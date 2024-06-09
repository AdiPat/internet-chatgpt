import copy
import urllib.parse
import openai
import requests
import urllib
import traceback
import os
from openai.types.chat.chat_completion import ChatCompletion

ai = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def search_internet(query: str) -> str:
    """Searches the Internet for a query and returns a markdown response of the results"""
    try:
        url = f"https://s.jina.ai/{urllib.parse.quote(query)}"
        response = requests.get(url)
        return response.text
    except Exception as e:
        traceback.print_exc()
        return None


def get_search_query(messages: list) -> str:
    """Get the search query from the messages"""
    updated_messages = copy.deepcopy(messages)
    updated_messages.append(
        {
            "role": "user",
            "content": "For the given conversation, generate a search query that can be used to search the internet for more information. Response in the format Query: <search query>.",
        }
    )
    response = ai.chat.completions.create(model="gpt-4o", messages=updated_messages)
    query = response.choices[0].message.content.split(":")[1]
    return query


def chat(*args, **kwargs) -> ChatCompletion:
    """Chat with the AI using OpenAI's GPT-3 model"""
    messages = kwargs.get("messages", [])

    query = get_search_query(messages)

    print("query: ", query)

    search_results = search_internet(query)

    messages.extend(
        [
            {
                "role": "user",
                "content": f"Context: {search_results}",
            },
        ]
    )

    kwargs["messages"] = messages

    response = ai.chat.completions.create(*args, **kwargs)

    return response
