# Read from the input file and write to the output file

def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read all content of the file

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)  # Write modified content to new file

        print("File has been modified and saved as", output_filename)

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file = 'files/input.txt'
output_file = 'files/output.txt'
read_and_write_file(input_file, output_file)
