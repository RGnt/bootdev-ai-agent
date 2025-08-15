import os
import subprocess


def run_python_file(working_directory, file_path="", args=None):
    if args is None:
        args = []

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.endswith(('.py')):
        return f'Error: "{file_path}" is not a Python file.'

    exec_proc = ['python', f'{abs_file_path}']
    if len(args) > 0:
        exec_proc.extend(args)

    try:
        print("Starting execution")
        completed_process = subprocess.run(exec_proc, cwd=abs_working_dir, timeout=30)

        output = f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\n'

        if completed_process.returncode != 0:
            output += f'Error: Process exited with code {completed_process.returncode}\n'

        return output

    except Exception as e:
        return f'Error: executing python file: {e}\n'