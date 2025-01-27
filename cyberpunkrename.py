import os

def rename_pdfs():
    # Strings to remove from filenames
    strings_to_remove = ['RTG', 'DLC', 'CX']

    # Get the current working directory
    directory = os.getcwd()

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a PDF
        if filename.endswith('.pdf'):
            new_name = filename
            # Remove unwanted strings
            for s in strings_to_remove:
                new_name = new_name.replace(s, '')
            # Trim whitespace from the new name
            new_name = new_name.strip()
            # Rename the file if the name has changed
            if new_name != filename:
                original_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)
                os.rename(original_path, new_path)
                print(f"Renamed: '{filename}' -> '{new_name}'")
            else:
                print(f"No changes needed: '{filename}'")

# Run the function
if __name__ == "__main__":
    rename_pdfs()