from agents import Agent, Runner,OpenAIChatCompletionsModel,Runner,set_tracing_disabled
from openai import AsyncOpenAI
import asyncio
from dotenv import load_dotenv
import os 

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

#Reference: https://ai.google.dev/gemini-api/docs/openai)

client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_tracing_disabled(True)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    
)

    result = await Runner.run(
        agent,
        "Tell me about recursion in programming.",
    )
    print(result.final_output)

    

asyncio.run(main())

