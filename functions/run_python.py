import os
import subprocess
import sys
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    rel_path = os.path.join(working_directory, file_path)
    target = os.path.realpath(os.path.abspath(rel_path))
    root = os.path.realpath(os.path.abspath(working_directory))

    if not target.startswith(root + os.sep) or target == root:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target):
        return f'Error: File "{file_path}" not found.'
    if not target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(
            [sys.executable, target, *args], capture_output=True, timeout=30
        )
        if not completed_process:
            return f"No output produced"
        if completed_process.returncode != 0:
            return f"STDOUT: {completed_process.stdout} \n STDERR: {completed_process.stderr} Process exited with code {completed_process.returncode}"
        return (
            f"STDOUT: {completed_process.stdout} \n STDERR: {completed_process.stderr}"
        )
    except Exception as e:
        return f"Error: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a python file with optional arguments in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="The arguments to be used while executing the file.",
            ),
        },
    ),
)
