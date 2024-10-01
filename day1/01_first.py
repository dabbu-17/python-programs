import os

def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")


# Example usage
directory_path = "/Users/SONY"  # Replace with your directory path
print_directory_contents(directory_path)
