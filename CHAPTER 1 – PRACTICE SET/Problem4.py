import os

def list_directory_contents(directory_path):
    """
    Function to list the contents of a directory.

    Args:
    directory_path (str): The path of the directory to list contents of.

    Returns:
    None
    """
    try:
        # Get the list of all files and directories in the specified directory
        dir_contents = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        # Loop through the directory contents and print each item
        for item in dir_contents:
            print(item)
    except FileNotFoundError:
        # Handle the error if the directory does not exist
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        # Handle the error if there is a permission issue accessing the directory
        print(f"Permission denied to access the directory '{directory_path}'.")
    except OSError as e:
        # Handle any other OS-related errors
        print(f"An OS error occurred: {e}")

# Prompt the user to enter the directory path
directory_path = input("Enter the path of the directory: ")
# Call the function to list the directory contents
list_directory_contents(directory_path)
