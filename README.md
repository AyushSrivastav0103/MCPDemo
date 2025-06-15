# MCPDemo

A demo project showcasing the use of MCP (Multi-Channel Platform) agent with browser automation and Groq LLM integration.

## Features
- Chat with an agent that can use browser automation, Airbnb, and DuckDuckGo tools
- Powered by Groq's Llama 3 model for fast, high-quality responses
- Easily extensible with new tools via `browser_mcp.json`

## Usage
- Type your queries in the console (e.g., "open google", "provide me some hotel listings to stay in New York").
- Type `exit` to end the chat.
- Type `clear` to clear the conversation memory.

## Configuration
- The `browser_mcp.json` file defines which MCP servers/tools are available to the agent.
- You can add or modify tools by editing this file.

## Notes
- Be aware of Groq API rate limits if using a free API key. See [Groq Rate Limits](https://console.groq.com/docs/rate-limits).
- For browser and Airbnb automation, ensure you have the necessary permissions and API keys if required.

## License
MIT