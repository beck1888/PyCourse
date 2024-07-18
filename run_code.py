import subprocess

def run_python_code(code):
    """
    Executes the given Python code and returns its output.
    
    Parameters:
    code (str): The Python code to be executed as a string.
    
    Returns:
    dict: A dictionary with keys 'errors' and 'output'. 'errors' is a boolean indicating
          if an error occurred, and 'output' contains the standard output or error message.
    """
    try:
        # Run the Python code using a subprocess
        result = subprocess.run(
            ['python3', '-c', code],  # Use 'python3' to run the code
            capture_output=True,      # Capture the output of the command
            text=True,                # Return the output as a string
            check=True                # Raise an error if the command fails
        )
        return {"errors": False, "output": result.stdout + result.stderr}  # Return both stdout and stderr
    except subprocess.CalledProcessError as e:
        return {"errors": True, "output": e.stderr}  # Return the error message if an exception occurs
