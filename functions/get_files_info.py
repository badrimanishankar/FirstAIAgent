import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def get_files_info(working_directory, directory="."):
    rel_path = os.path.join(working_directory, directory)
    target = os.path.realpath(os.path.abspath(rel_path))
    root = os.path.realpath(os.path.abspath(working_directory))
    if target.startswith(root + os.sep) or target == root:

        if not os.path.isdir(target):
            return f'Error: "{directory}" is not a directory'

        target_list = os.listdir(target)
        lines = []
        for entry in target_list:
            entry_path = os.path.join(target, entry)
            is_dir = os.path.isdir(entry_path)
            entry_size = os.path.getsize(entry_path)
            lines.append(f" - {entry}: file_size={entry_size} bytes, is_dir={is_dir}")

        return "\n".join(lines)
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
