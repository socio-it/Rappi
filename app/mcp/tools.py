from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="FastAPI MCP Server")

@mcp.tool()
def ping() -> str:
    return "alive"

@mcp.tool()
def sum(a: float, b: float) -> float:
    return a + b

# mcp 1.17 -> usar transporte SSE
mcp_app = mcp.sse_app()  # OJO: llamado como función
