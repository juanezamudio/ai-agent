import os
import config

def get_file_content(working_directory, file_path):
    working_directory_full_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if not full_path.startswith(working_directory_full_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, 'r') as file:
            content = file.read(config.MAX_FILE_SIZE)

            if os.path.getsize(full_path) > config.MAX_FILE_SIZE:
                content += f"[...File \"{file_path}\" truncated at {config.MAX_FILE_SIZE} characters]"

            return content

    except ValueError as e:
        return f"Error: {e}"
        
            