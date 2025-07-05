<!-- @format -->

# AI SQL Agent (MCP)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A sophisticated command-line AI agent that understands natural language and interacts with a local SQLite database. This project uses the Model Context Protocol (MCP) to create a secure, decoupled architecture where the AI "brain" and the database "tool" operate as separate processes.

This agent is powered by Anthropic's Claude 3.5 Sonnet model for advanced reasoning and tool-use capabilities.

---

## ✨ Features

- **Natural Language to SQL:** Interact with your database using plain English queries.
- **Secure, Decoupled Architecture:** The core AI logic is completely separated from the database-accessing tool, ensuring that sensitive credentials and operations are sandboxed.
- **Intelligent Tool Use:** Leverages Claude 3.5 Sonnet's function-calling to dynamically decide when to execute SQL queries based on the user's request.
- **Extensible Toolset:** Designed to be easily extended. New tools can be added to `mcp_server.py` with a simple `@mcp.tool()` decorator and are automatically discovered by the client.
- **Interactive & Robust CLI:** A clean command-line interface for conversation, with graceful handling of user exits (`Ctrl+C`).

## 🛠️ Tech Stack

- **AI Model:** Anthropic Claude 3.5 Sonnet
- **Protocol:** Model Context Protocol (MCP)
- **Database:** SQLite
- **Core Libraries:** `mcp`, `anthropic`, `python-dotenv`, `loguru`
- **Package Management:** `uv`

## 🚀 Installation and Configuration

Get the agent running on your local machine in a few simple steps.

### 1. Clone the Repository

```bash
git clone https://github.com/SUKESH127-art/mcp-sql-agent.git
cd mcp-sql-agent
```

## ▶️ Usage

### 1. Run the Agent

Start the main client script. It will automatically launch and manage the server process for you.

```bash
python3 mcp_client.py
```

### 2. Start Chatting!

Once running, you can interact with the agent. To exit at any time, press `Ctrl+C`.

**Example Queries:**

- `"Show me all the users in the database."`
- `"How many users are there?"`
- `"What is the email for Ada Lovelace?"`
- `"Can you create a new user named 'John Doe' with the email 'john.d@example.com'?"`
- `"Show me all users whose email ends with .com"`

---

## 🔧 Development & Testing

For debugging or testing the server's tools in isolation, you can use the built-in MCP Inspector.

1.  **Activate the Virtual Environment:**

    ```bash
    source .venv/bin/activate
    ```

2.  **Run the Server in Dev Mode:**
    This command starts the server and hosts the web inspector.

    ```bash
    mcp dev mcp_server.py
    ```

3.  **Open the Inspector:**
    Your terminal will show a line like `Uvicorn running on http://127.0.0.1:8000`. Open that URL in your web browser.

4.  **Test Tools Manually:**
    You can now directly invoke the `query_data` tool from the web interface to test its functionality without needing the AI client.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the agent or add new features:

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📝 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
