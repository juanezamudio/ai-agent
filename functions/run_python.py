import os
import subprocess
import config

def run_python_file(working_directory, file_path, args=[]):
    working_directory_full_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if not full_path.startswith(working_directory_full_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'

        if not full_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        commands = ["python3", f"{full_path}"] + args

        completed_process = subprocess.run(
            commands,
            cwd = working_directory_full_path,
            capture_output=True,
            text=True, 
            timeout=config.MAX_EXECUTION_TIME
        )

        if completed_process.returncode != 0:
            return f'Process exited with code {completed_process.returncode}'
            
        if not completed_process.stdout.strip():
            return f'No output produced'

        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n {completed_process.stdout.strip()}")
        if completed_process.stderr:
            output.append(f"STDERR:\n {completed_process.stderr.strip()}")
        
        return '\n'.join(output) if output else 'No output produced'

    except subprocess.TimeoutExpired:
        return f'Error: Execution timed out'

    except Exception as e:
        return f'Error: executing Python file {e}'

        
        