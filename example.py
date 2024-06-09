from dotenv import load_dotenv

load_dotenv()

from internet_chatgpt import chat


completion = chat(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a weather assistant.",
        },
        {
            "role": "user",
            "content": "What's the weather in Mumbai right now?",
        },
    ],
)

print(completion.choices[0].message.content)

completion = chat(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a IT assistant.",
        },
        {
            "role": "user",
            "content": "How to install Windows 11. Give detailed steps.",
        },
    ],
)

print(completion.choices[0].message.content)
