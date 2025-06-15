"""Simple chat using MCP that has features of a browser automation agent
This script uses the MCPClient to connect to the browser automation agent.
It uses the ChatGroq model to generate responses.
It uses the MCPAgent to manage the conversation and the tools.
It uses the MCPClient to connect to the browser automation agent.
It uses the ChatGroq model to generate responses.
It uses the MCPAgent to manage the conversation and the tools.
"""
import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from mcp_use import MCPAgent,MCPClient

async def run__mem_chat():
    """
    Run a memory chat with the user.
    """
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is not set")
    
    config_file="browser_mcp.json"
    print(f"Loading MCP client from {config_file}")
    print("Initializing Chat")
    client = MCPClient.from_config_file(config_file)

    llm = ChatGroq(model="llama3-8b-8192",api_key=groq_api_key)
    
    agent = MCPAgent(
        client=client,
        llm=llm,
        max_steps=15,
        memory_enabled=True,     #enable memory
    )

    print("Starting Chat")
    print("Type 'exit' to end the chat")
    print("Type 'help' to get help")
    print("Type 'clear' to clear the memory")

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting Chat")
                break
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Memory Cleared")
                continue

            print("Assistant",end="",flush=True)

            try:
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"Error: {e}")
                continue
    finally:
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run__mem_chat())

