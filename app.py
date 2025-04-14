from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

client = OpenAI()

message_history = []

def append_to_message_history(history, role, content):
    history.append({"role": role, "content": content})

blue = "\033[34m"
red = "\033[31m"
bold = "\033[1m"

def change_text(text, style):
    return style + text + "\033[0m"

def main():
    parser = argparse.ArgumentParser(description="Simple command line chatbot with Chat GPT")
    parser.add_argument("--personality", type=str, default="friendly and helpful chatbot", help="A brief summary of the chatbot's personality")
    args = parser.parse_args()
    
    append_to_message_history(message_history, "system", "You're a conversational chatbot. Your personality is: " + args.personality)

    while True:
        try:
            user_input = input(change_text("You: ", blue))
            append_to_message_history(message_history, "user", user_input)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=message_history
            )
            append_to_message_history(message_history, "assistant", response.choices[0].message.content)
            print(change_text("Assistant: ", bold), change_text(response.choices[0].message.content, red))

        except KeyboardInterrupt:
            print("Quitting")
            break

if __name__ == "__main__":
    main()

