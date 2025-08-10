import os
import subprocess
import config
from google import genai

def run_python_file(working_directory, file_path, args=[]):
    working_directory_full_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    print(f"DEBUG: abs_working_dir = {working_directory_full_path}")
    print(f"DEBUG: abs_file_path = {full_path}")
    print(f"DEBUG: file exists = {os.path.exists(full_path)}")

    try:
        if not full_path.startswith(working_directory_full_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'

        if not full_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        commands = ["python3", f"{full_path}"] + args

        print(f"DEBUG: Running command: {commands}")
        print(f"DEBUG: Working directory: {working_directory_full_path}")

        completed_process = subprocess.run(
            commands,
            cwd = working_directory_full_path,
            capture_output=True,
            text=True, 
            timeout=config.MAX_EXECUTION_TIME
        )

        print(f"DEBUG: Return code: {completed_process.returncode}")
        print(f"DEBUG: STDOUT: '{completed_process.stdout}'")
        print(f"DEBUG: STDERR: '{completed_process.stderr}'")

        if completed_process.returncode != 0:
            return f'Process exited with code {completed_process.returncode}'

        output = []

        if completed_process.stdout.strip():
            output.append(f"STDOUT:\n {completed_process.stdout.strip()}")

        if completed_process.stderr.strip():
            output.append(f"STDERR:\n {completed_process.stderr.strip()}")
        
        print(f"DEBUG: output list: {output}")
        print(f"DEBUG: output list length: {len(output)}")

        return '\n'.join(output) if output else 'No output produced'

    except subprocess.TimeoutExpired:
        return f'Error: Execution timed out'

    except Exception as e:
        return f'Error: executing Python file {e}'

schema_run_python_file = genai.types.FunctionDeclaration(

    name="run_python_file",
    description="Runs a Python file in the specified file path, constrained to the working directory and max execution time.",
    
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to run, relative to the working directory.",
            ),
            "args": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                items=genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                description="Arguments to pass to the Python file.",
            ),
        },
    ),
)