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
