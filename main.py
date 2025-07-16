from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


translator_agent= Agent(
    name= "Translator Agent",
    instructions="You are a multilingual translator. Translate input text into English,french and Chinese."
)


response = Runner.run_sync(
    translator_agent,
    input= "الفاظ وہ آئینہ ہیں جن میں دل کی تصویر نظر آتی ہے, translate into english, chinese",
    run_config=config
)

print(response.final_output)


