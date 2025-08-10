import os
from dotenv import load_dotenv
from google import genai
import sys
import config
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"- Calling function: {function_call_part.name}({function_call_part.args})\n")
    else:
        print(f"- Calling function: {function_call_part.name}")

    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if function_call_part.name not in function_map:
        return genai.types.Content(
            role="tool",
            parts=[
                genai.types.Part.from_function_response(
                    name = function_call_part.name,
                    response = {"error": f"Unknown function: {function_call_part.name}"}
                )
            ]
        )

    args = dict(function_call_part.args)
    args["working_directory"] = config.WORKING_DIRECTORY

    try:
        result = function_map[function_call_part.name](**args)

        return genai.types.Content(
            role = "tool",
            parts = [
                genai.types.Part.from_function_response(
                    name = function_call_part.name,
                    response = {"result": result}
                )
            ]
        )
    except Exception as e:
        return genai.types.Content(
            role="tool",
            parts=[
                    genai.types.Part.from_function_response(
                    name = function_call_part.name,
                    response = {"error": f"Function call failed: {function_call_part.name}"}
                )
            ]
        )

def generate_content(client, messages, verbose):
    available_functions = genai.types.Tool(
        function_declarations = [
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=genai.types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=config.SYSTEM_PROMPT
        ),
    )

    if response.candidates:
        for candidate in response.candidates:
            print(f"Candidate: {candidate.content.parts[0].text}")
            messages.append(candidate.content)
    
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # If there are no function calls, return the text response
    if not response.function_calls:
        return response.text
    
    # Handle all function calls
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)

        if not function_call_result.parts or not function_call_result.parts[0].function_response:
            raise Exception("empty function call result")

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("No function responses generated, exiting")
    
    # Add function responses to messages and continue conversation
    messages.append(genai.types.Content(
        role="tool",
        parts=function_responses
    ))

    return None
    
def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    args = []
    verbose = "--verbose" in sys.argv

    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)])
    ]

    # Loop up to MAX_ITERATIONS times to call generate_content to get the final response
    counter = 0
    while True:
        counter += 1

        if counter > config.MAX_ITERATIONS:
            print(f"Max iterations reached: {counter}")
            break

        try:
            final_response = generate_content(client, messages, verbose)

            if final_response:
                print(f"-> {final_response}")
                break

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
