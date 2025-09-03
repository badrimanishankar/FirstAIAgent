import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    rel_path = os.path.join(working_directory, file_path)
    target = os.path.realpath(os.path.abspath(rel_path))
    root = os.path.realpath(os.path.abspath(working_directory))

    if not target.startswith(root + os.sep) or target == root:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)
            if len(file_content_string) > MAX_CHARS:
                return f'{file_content_string[:MAX_CHARS]} [...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads file contents in the specified directory truncated at 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read the file from, relative to the working directory.",
            ),
        },
    ),
)
