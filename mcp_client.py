import asyncio
import anthropic
from dataclasses import dataclass, field
from typing import Union, cast
from anthropic.types import MessageParam, TextBlock, ToolUnionParam, ToolUseBlock
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Load the anthropic key from .env
load_dotenv()

# initialize the client to communicate with anthropic API
anthropic_client = anthropic.AsyncAnthropic()

# define how to start local MCP server
server_params = StdioServerParameters(
    command="python",
    args=["./mcp_server.py"]
)

@dataclass
class Chat:
    """Class to manage the state and flow of chat conversation."""

    messages: list[MessageParam] = field(default_factory=list)

    system_prompt: str = """ 
        You are a master SQLite assistant. 
        Your job is to use the tools at your disposal to execute SQL queries 
        and provide the results to the user. 
    """
    
    async def process_query(self, session: ClientSession, query: str) -> None:
        """Processes a single user query, interacts with AI, and handles tool calls."""
        
        # Discover tools from server
        response = await session.list_tools()
        available_tools: list[ToolUnionParam] = [
            {
                "name": tool.name,
                "description": tool.description or "",
                "input_schema": tool.inputSchema
            } 
            for tool in response.tools
        ]
        
        # Ask AI, send our prompt, convos, tool options -> use tool or not?
        res = await anthropic_client.messages.create(
            model="claude-3-5-sonnet-latest",
            system=self.system_prompt,
            max_tokens=8000,
            messages=self.messages,
            tools=available_tools
        )
        
        assistant_message_content: list[Union[ToolUseBlock, TextBlock]] = []
        for content in res.content:
            # if AI response, is just text, print!
            if content.type == "text":
                assistant_message_content.append(content)
                print(content.text)
            # we need to use our tools
            elif content.type == "tool_use":
                tool_name = content.name
                tool_args = content.input
                assistant_message_content.append(content)
            
                # execute tool call on server
                result = await session.call_tool(tool_name, cast(dict, tool_args))
                # add assistant action & result to convo 
                self.messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_message_content
                    }
                )
                
                self.messages.append(
                    {
                        "role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": content.id,
                            "content": getattr(result.content[0],"text","")
                        }]
                    }
                )
                
                # make second API call with tool result for final summary
                final_res = await anthropic_client.messages.create(
                    model="claude-3-7-sonnet-latest",
                    max_tokens=8000,
                    messages=self.messages,
                    tools=available_tools,
                )
                
                self.messages.append(
                    {
                        "role": "assistant",
                        "content": getattr(res.content[0], "text", "")
                    }
                )
                final_text = getattr(final_res.content[0], "text", "")
                self.messages.append({"role": "assistant", "content": final_text})
                print(final_text)
    
    async def chat_loop(self, session: ClientSession):
        """The main chat loop to get user input and process it"""
        while True:
            query = input("\nQuery: ").strip()
            if not query:
                continue
            self.messages.append(MessageParam(role="user", content=query))
            # call the main processing here
            print("\nQuery Received! Processing logic to be added...")
            await self.process_query(session, query)
            
    async def run(self):
        """Starts the server, connects to client, and runs the chat loop."""
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("MCP Client & Server running!\n")
                await self.chat_loop(session)

if __name__ == "__main__":
    try:
        chat = Chat()
        # start entire application
        asyncio.run(chat.run())
    except KeyboardInterrupt:
        print("\n\nExiting gracefully. Goodbye!\n\n")