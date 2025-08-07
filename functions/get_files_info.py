import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    working_directory_full_path = os.path.abspath(working_directory)

    dir_display = 'current' if directory == '.' else f"'{directory}'"
    result_display = f"Result for {dir_display} directory:"

    try:
        common_path = os.path.commonpath([full_path, working_directory_full_path])

        if common_path != working_directory_full_path:
            return f"{result_display}\nError: Cannot list '{directory}' as it is outside the permitted working directory"

    except ValueError as e:
        return f"{result_display}\nError: Cannot list '{directory}' as it is outside the permitted working directory"

    if not os.path.isdir(full_path):
        return f"{result_display}\nError: '{directory}' is not a directory"

    try:
        files = sorted(os.listdir(full_path))
        result = [result_display]

        for file in files:
            if file.startswith("__pycache__"):
                continue

            file_path = os.path.join(full_path, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)

            string = f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
            result.append(string)

        return "\n".join(result)

    except Exception as e:
        return f"Error: {e}"


