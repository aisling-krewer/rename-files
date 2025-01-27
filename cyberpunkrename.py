import os

def rename_pdfs():
    # Strings to remove from filenames
    # Will remove hardcoding at a later date
    strings_to_remove = ['RTG', 'DLC', 'CX', '-', 'CPR', 'v1.11', 'v1.1', 'v1.0', 'v2', 'CEMK', 'LTR']
    #Couldn't find a more straighforward way of defining words to be separated.
    #Works great for my cyberpunk files, may need to rethink for other files
    add_space = ['Cyberpunk', 'Blackhands', 'Black', 'All', 'About', 'Chrome', 'Street', 'Weapons', 'Breaking',
                 'Your', 'Stuff', 'Chasing', 'the', 'Chromebook', '1', '2', 'and', '3', 'corporation', 'report',
                 '2020', 'core', 'Cyberware', 'Danger', 'gal', 'Did', 'Someone', 'Say', 'Dreaded', 'Eurosource',
                 'home', 'of', 'hope', 'reborn', 'Hornets', 'Interface', 'Vol', 'listen', 'Mixing', 'Drinks', 'Changing',
                 'Night', 'No', 'Place', 'Like', 'Pacific', 'Rough', 'Guide', 'to', 'the', 'Screamsheet', 'Tales', 'Forlorn',
                  'street', 'Toggles', 'Temple', 'TotR', 'New', 'Best', 'tales']
    
    # Get the current working directory
    # I'm calling this portable, not being lazy.
    directory = os.getcwd()

    # Iterate through all files in the directory
    #TODO: This process is missing files within directories. 
    for filename in os.listdir(directory):
        # Check if the file is a PDF
        # Focus is for Kavita library, may update later
        if filename.endswith('.pdf'):
            new_name = filename
            # Remove unwanted strings
            for s in strings_to_remove:
                new_name = new_name.replace(s, '')
            # Trim whitespace from the new name
            new_name = new_name.strip()
            # Add spaces to the new name
            for s in add_space:
                #check s isn't right before or after a space, or just before .pdf
                if s + ' ' not in new_name and ' ' + s not in new_name and s != new_name[-4:]:
                    new_name = new_name.replace(s, s + ' ') 
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
