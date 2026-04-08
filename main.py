import os

from fastmcp import FastMCP
from fastmcp.server.auth.providers.debug import DebugTokenVerifier

API_TOKEN = os.environ.get("API_TOKEN", "")

verifier = DebugTokenVerifier(
    validate=lambda token: bool(API_TOKEN) and token == API_TOKEN,
    client_id="hello-world-client",
    scopes=["read"],
)

mcp = FastMCP(name="Hello World", auth=verifier)


@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8111)
