.PHONY: install run dev help

API_TOKEN ?= dev-secret-token

help:
	@echo "Usage:"
	@echo "  make install   Install dependencies"
	@echo "  make run       Run the MCP server (set API_TOKEN env var)"
	@echo "  make dev       Run with a default dev token"

install:
	uv sync

run:
	API_TOKEN=$(API_TOKEN) uv run python main.py

dev:
	API_TOKEN=$(API_TOKEN) uv run fastmcp dev main.py
