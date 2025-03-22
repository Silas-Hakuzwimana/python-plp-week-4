# Handle file errors gracefully by asking the user for a filename

def get_file_content():
    filename = input("Enter the filename to read: ")
    try:
        # Try opening the file in read mode
        with open(filename, 'r') as file:
            content = file.read()  # Read all content of the file
            print("File content:\n", content)

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: The file {filename} can't be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
get_file_content()
