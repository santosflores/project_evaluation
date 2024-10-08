#!/usr/bin/env python3

"""
Document summarizer. Create a cliff notes-like effective compression of a document.
Useful Links

1. LangSmith @traceable decorator docs -> https://docs.smith.langchain.com/old/cookbook/tracing-examples/traceable#using-the-decorator

"""
import chainlit.user
from prompt import SYSTEM_PROMPT
import chainlit
import openai
import os

from dotenv import load_dotenv
from langsmith import traceable
from langsmith.wrappers import wrap_openai

load_dotenv()


openai_config = {
    "endpoint_url": os.getenv("OPENAI_ENDPOINT"),
    "api_key": os.getenv("OPENAI_API_KEY"),
    "model": "gpt-4o-mini",
}

gen_kwargs = {"model": openai_config["model"], "temperature": 0.3, "max_tokens": 500}

client = wrap_openai(
    openai.AsyncClient(
        api_key=openai_config["api_key"], base_url=openai_config["endpoint_url"]
    )
)


def initialize_bot():
    message_history = chainlit.user_session.get("message_history", [])
    # If no previous interaction. Add the SYSTEM_PROMPT as the first message,
    # this will allow the bot to understand its role in the conversation
    if len(message_history) == 0:
        message_history.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
        chainlit.user_session.set("message_history", message_history)


@traceable(run_type="llm")
async def get_gpt_response_stream(request):
    message_history = chainlit.user_session.get("message_history", [])
    # Add the new message from the end-user to message_history
    message_history.append(request)
    # Create a new response
    response = chainlit.Message(content="")
    # Creates GPT client to send the end-user request
    stream = await client.chat.completions.create(
        messages=message_history, stream=True, **gen_kwargs
    )
    # Get GPT response via streaming
    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await response.stream_token(token)
    # Add GPTs response to message_history
    message_history.append({"role": "assistant", "content": response.content})
    # Add the entire conversation to the session context. This allows the model
    # to have message history available
    chainlit.user_session.set("message_history", message_history)
    # Send the response to the end-user
    await response.send()


@traceable(run_type="chain")
@chainlit.on_chat_start
async def on_chat_start():
    initialize_bot()
    await get_gpt_response_stream(
        {
            "role": "system",
            "content": """Say hello to the end-user. Make sure you let them know 
            your function.""",
        }
    )


@traceable(run_type="chain")
@chainlit.on_message
async def on_message(message: chainlit.Message):
    # Add the new message from the end-user to message_history
    await get_gpt_response_stream({"role": "user", "content": message.content})


if __name__ == "__main__":
    chainlit.main()
