import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print(response.text)

if __name__ == "__main__":
    main()
