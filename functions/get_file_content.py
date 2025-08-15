import os
from functions.config import CHARACTERS_LIMIT

def get_file_content(working_directory="", file_path=""):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        file_content_string = ""
        with open(abs_file_path, "r") as file:
            file_content_string = file.read(CHARACTERS_LIMIT)
            if os.path.getsize(abs_file_path) > CHARACTERS_LIMIT:
                file_content_string += f'\n[... File "{file_path}" truncated at {CHARACTERS_LIMIT} characters'

        return  file_content_string
    except Exception as e:
        return f'Error: {e}'