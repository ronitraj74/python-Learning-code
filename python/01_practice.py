import os

# Specify the directory you want to list
directory_path = "code"

try:
    # List all files and directories
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except NotADirectoryError:
    print(f"Error: '{directory_path}' is not a directory.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")
