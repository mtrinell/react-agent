from src.react_agent import graph
from langchain_openai import AzureChatOpenAI
import asyncio
import os
from dotenv import load_dotenv

async def main():
    res = await graph.ainvoke(
        {"messages": [("user", "Who is the founder of LangChain?")]},
        {"configurable": {"system_prompt": "You are a helpful AI assistant."}},
    )
    print(res)

if __name__ == "__main__":
    asyncio.run(main())