import os
from google.genai import types


def write_file(working_directory, file_path, content):
    rel_path = os.path.join(working_directory, file_path)
    target = os.path.realpath(os.path.abspath(rel_path))
    root = os.path.realpath(os.path.abspath(working_directory))
    target_dir = os.path.dirname(target)
    if not target.startswith(root + os.sep) or target == root:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    try:
        with open(target, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Reads file contents in the specified directory truncated at 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path where the file exists, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content being written to the file.",
            ),
        },
    ),
)
