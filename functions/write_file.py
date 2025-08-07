import os

def write_file(working_directory, file_path, content):
    working_directory_full_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if not full_path.startswith(working_directory_full_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(full_path):
            os.makedirs(os.path.dirname(file_path))

        if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
            return f'Error: "{file_path}" is a directory, not a file'

        with open(full_path, 'w') as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
        