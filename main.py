"""
main.py
--------
Entry point for the MCP server using FastAPI and context7.
"""
from fastapi import FastAPI, HTTPException, Request
from typing import Dict

app = FastAPI(title="MCP Server")

# In-memory resource and tool registries for demonstration
resources = {
    "llm-demo": {
        "id": "llm-demo",
        "type": "llm",
        "name": "Demo LLM",
        "description": "A mock LLM resource for MCP testing.",
        "provider": "demo",
        "capabilities": ["completion"]
    }
}

tools = {
    "calculator": {
        "id": "calculator",
        "type": "function",
        "name": "Calculator",
        "description": "A simple calculator tool.",
        "parameters": [
            {"name": "a", "type": "number"},
            {"name": "b", "type": "number"},
            {"name": "operation", "type": "string", "enum": ["add", "subtract", "multiply", "divide"]}
        ]
    }
}

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

# Resource endpoints
@app.get("/resources")
def list_resources():
    """List all available MCP resources."""
    return {"resources": list(resources.values())}

@app.get("/resource/{resource_id}")
def get_resource(resource_id: str):
    """Get metadata for a specific resource."""
    resource = resources.get(resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@app.post("/resource/{resource_id}/invoke")
async def invoke_resource(resource_id: str, request: Request):
    """Invoke a resource (e.g., run an LLM completion)."""
    resource = resources.get(resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    data = await request.json()
    # Demo: just echo input and mock output
    return {"resource_id": resource_id, "input": data, "output": "This is a mock response from the MCP resource."}

# Tool endpoints
@app.get("/tools")
def list_tools():
    """List all available MCP tools."""
    return {"tools": list(tools.values())}

@app.get("/tool/list")
def list_tools_alt():
    """Alternative endpoint for listing tools (for OpenAI Responses API compatibility)."""
    return {"tools": list(tools.values())}

@app.get("/tool/{tool_id}")
def get_tool(tool_id: str):
    """Get metadata for a specific tool."""
    tool = tools.get(tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool

@app.post("/tool/{tool_id}/invoke")
async def invoke_tool(tool_id: str, request: Request):
    """Invoke a tool (e.g., function call)."""
    tool = tools.get(tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    data = await request.json()
    # Demo: calculator tool logic
    if tool_id == "calculator":
        a = data.get("a")
        b = data.get("b")
        op = data.get("operation")
        result = None
        if op == "add":
            result = a + b
        elif op == "subtract":
            result = a - b
        elif op == "multiply":
            result = a * b
        elif op == "divide":
            result = a / b if b != 0 else None
        else:
            result = "Invalid operation"
        return {"tool_id": tool_id, "input": data, "result": result}
    # Default mock
    return {"tool_id": tool_id, "input": data, "result": "This is a mock response from the MCP tool."}
