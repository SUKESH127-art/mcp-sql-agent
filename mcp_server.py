import sqlite3
from loguru import logger  # <-- It's imported here
from mcp.server.fastmcp import FastMCP

# create mcp server instance named demo
mcp = FastMCP("SQLToolServer")

# decorator: expose the mcp tool
@mcp.tool()
def query_data(sql: str) -> str:
    """Execute SQL safely"""
    # This line uses loguru to print a timestamped, informative log
    logger.info(f"Executing SQL query: {sql}")
    # connect to local db file. 
    conn = sqlite3.connect("./database.db")
    try:
        # execute the query and fetch results
        result = conn.execute(sql).fetchall()
        conn.commit()
        # format results intp single string for AI
        return formatStringForAI(result)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        # ensure connection is always closed
        conn.close()

def formatStringForAI(input):
    # formats everything into a single string
    return "\n".join(str(row) for row in input)


if __name__ == "__main__":
    print("Starting mcp server...")
    # initialize and run server, communicating over standard I/O
    mcp.run(transport="stdio")