from src.react_agent import graph
from langchain_openai import AzureChatOpenAI
import asyncio
import os
from dotenv import load_dotenv


async def main():
    config = {"configurable": {
        "system_prompt": "Answer in italian",
        "model": "azure_openai/gpt-4o-mini"
    }}

    async for event in graph.astream({"messages": [("user", "Who is the founder of LangChain?")]}, config=config):
        for k, v in event.items():
            if k != "__end__":
                print(k, v)
                print()

if __name__ == "__main__":
    asyncio.run(main())
