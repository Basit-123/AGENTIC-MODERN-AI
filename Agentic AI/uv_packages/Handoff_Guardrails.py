from agents import(
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    RunConfig,
    handoff
)

from openai import AsyncOpenAI
import rich
gemini_api_key = "AIzaSyBEhh-3_BapBw9OVjGo2cgtntfWU7P_31s"

#Reference: https://ai.google.dev/gemini-api/docs/openai

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model = model,
    model_provider=external_client,
    tracing_disabled= True
)


billing_agent = Agent(
    name = "Refund Agent",
    instructions = "You handle all billing-related inquiries. Provide clear and concise information regarding billing issues.",
)

refund_agent = Agent(
    name = "Refund Agent",
    instructions = "You handle all "
)

triage_agent = Agent(
    name = "Triage Agent",
    instructions ="You determine which agent should handle the users request based on the nature if inquiry",
    handoffs= [billing_agent,refund_agent]
)


result = Runner.run_sync(
    starting_agent= billing_agent,
    input = "I need a a refund for my recent purchases.",
    run_config=config
)

print("last Agent>>>>", result.last_agent)
rich.print("result>>>>", result.final_output)