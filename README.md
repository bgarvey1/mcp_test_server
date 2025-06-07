# MCP Server with Context7

This project implements a Model Context Protocol (MCP) server using the context7 library and FastAPI. It is designed to be easily deployable on any external web host.

## Features
- MCP-compliant API endpoints
- FastAPI-based server
- Easy deployment (Docker-ready)

## Setup
1. `python -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload`

## Deployment
- Add deployment instructions for your chosen host (Docker, Render, etc.)

## References
- [MCP Spec](https://modelcontextprotocol.io/llms-full.txt)
- [context7](https://pypi.org/project/context7/)
