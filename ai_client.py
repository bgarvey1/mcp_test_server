"""
AI Client for MCP Calculator Server

This client uses the OpenAI Responses API to interact with an MCP calculator server.
It sends natural language math queries to the API and uses the MCP tool to execute calculations.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment or .env file.")

# MCP server URL - this is your deployed server on Render
MCP_SERVER_URL = "https://mcp-test-server-oq99.onrender.com"

client = OpenAI(api_key=OPENAI_API_KEY)

def main():
    """Main function to interact with the AI calculator."""
    print("AI Calculator Client ready! Type your math questions or 'quit' to exit.")
    print("Example: 'what is 5 plus 3?' or 'calculate 10 divided by 2'")
    
    while True:
        query = input("\nQuestion: ")
        if query.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        print("Using OpenAI Responses API with MCP...")
        try:
            response = client.responses.create(
                model="gpt-4",
                tools=[{
                    "type": "mcp",
                    "server_url": MCP_SERVER_URL,
                    "server_label": "calculator",
                    "require_approval": "never"
                }],
                input=query
            )
            
            # Extract text from the response
            if hasattr(response, "output") and hasattr(response.output, "text"):
                print(f"\nResult: {response.output.text}")
            else:
                print("No readable output in response")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()