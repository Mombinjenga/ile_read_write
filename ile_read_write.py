def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Ask the user for the output filename
        output_filename = input("Enter the name of the file to write to: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written.")

# Run the function
if __name__ == "__main__":
    read_and_write_file()