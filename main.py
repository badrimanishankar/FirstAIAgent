import os
from dotenv import load_dotenv
from google import genai
import sys


def main():

    print("Hello from agentchatbotcourse!")
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        is_verbose = False
        if len(sys.argv) > 2:
            if sys.argv[2] == "--verbose":
                is_verbose = True

        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=user_input,
        )
        if is_verbose:
            print(f"User prompt: {user_input}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
    else:
        print("No input provided")
        sys.exit(1)


if __name__ == "__main__":
    main()
