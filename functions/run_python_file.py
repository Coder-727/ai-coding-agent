import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory=os.path.abspath(working_directory)
    abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        final_args=["python3",file_path]
        final_args.extend(args)
        ouput=subprocess.run(
            final_args,
            cwd=abs_working_directory,
            timeout=30,
            capture_output=True
            )
        final_string= f"""
STDOUT: {ouput.stdout}
STDERR: {ouput.stderr}

"""
        if ouput.stdout=="" and ouput.stderr=="":
            final_string="No output produced.\n"
        if ouput.returncode!=0:
            final_string+=f'Process exited with code {ouput.returncode}'
        
        return final_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with python3 interpreter, Accepts additional CLI args as an optional array.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to run, from the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An Optional array of strings to be used as CLI args for the python file.",
                items=types.Schema(
                    type=types.Type.STRING
                ),
            ),
        },
    ),
)