"""
test_mcp_server.py
------------------
Simple script to test the local MCP server's endpoints for both resources and tools.
"""
import requests

BASE_URL = "http://127.0.0.1:8001"

def test_health():
    resp = requests.get(f"{BASE_URL}/health")
    print("/health:", resp.status_code, resp.json())

def test_list_resources():
    resp = requests.get(f"{BASE_URL}/resources")
    print("/resources:", resp.status_code, resp.json())

def test_list_tools():
    resp = requests.get(f"{BASE_URL}/tools")
    print("/tools:", resp.status_code, resp.json())

def test_invoke_tool():
    payload = {"a": 5, "b": 3, "operation": "multiply"}
    resp = requests.post(f"{BASE_URL}/tool/calculator/invoke", json=payload)
    print("/tool/calculator/invoke:", resp.status_code, resp.json())

def test_invoke_resource():
    payload = {"prompt": "Hello world"}
    resp = requests.post(f"{BASE_URL}/resource/llm-demo/invoke", json=payload)
    print("/resource/llm-demo/invoke:", resp.status_code, resp.json())

if __name__ == "__main__":
    test_health()
    test_list_resources()
    test_list_tools()
    test_invoke_tool()
    test_invoke_resource()
