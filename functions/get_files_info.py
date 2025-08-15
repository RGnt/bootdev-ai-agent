import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    final_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not os.path.exists(final_dir) and os.path.isdir(final_dir):
        return f'"{directory}" is not a directory'

    if not final_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        files_info = []
        for file in os.listdir(final_dir):
            filepath = os.path.join(final_dir, file)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
