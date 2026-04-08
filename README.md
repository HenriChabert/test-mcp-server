# Hello World MCP Server

A minimal [FastMCP](https://gofastmcp.com) server with Bearer token authentication.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
make install
```

## Run

```bash
API_TOKEN=your-secret-token make run
```

The server starts at `http://localhost:8111`.

## Dev mode (MCP Inspector)

```bash
API_TOKEN=your-secret-token make dev
```

Opens the MCP Inspector in the browser for interactive testing.

## Authentication

All requests must include the token as a Bearer header:

```
Authorization: Bearer your-secret-token
```

Requests without a valid token are rejected with `401 Unauthorized`.

## Tools

| Tool | Input | Output |
|------|-------|--------|
| `hello` | `name` (string, default: `"World"`) | `"Hello, {name}!"` |
