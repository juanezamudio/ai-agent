import os
from google import genai

def write_file(working_directory, file_path, content):
    working_directory_full_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if not full_path.startswith(working_directory_full_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))

        if os.path.exists(full_path) and os.path.isdir(full_path):
            return f'Error: "{file_path}" is a directory, not a file'

        with open(full_path, 'w') as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'

schema_write_file = genai.types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file in the specified file path, constrained to the working directory.",
    
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to write to, relative to the working directory.",
            ),
            "content": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)
    