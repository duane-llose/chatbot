from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

message_history = []

def append_to_message_history(history, role, content):
    history.append({"role": role, "content": content})

while True:
    try:
        user_input = input("You: ")
        append_to_message_history(message_history, "user", user_input)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message_history
        )
        append_to_message_history(message_history, "assistant", response.choices[0].message.content)
        print("Assistant: ", response.choices[0].message.content)

    except KeyboardInterrupt:
        print("Quitting")
        break