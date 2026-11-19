import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(
        "Missing OPENAI_API_KEY. Copy .env.example to .env and add your API key."
    )

client = OpenAI(api_key=api_key)

def main():
    print("AI Chatbot Starter")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("You: ").strip()
        if prompt.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not prompt:
            continue

        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )
            print(f"AI: {response.output_text}\n")
        except Exception as exc:
            print(f"Request failed: {exc}\n")

if __name__ == "__main__":
    main()
