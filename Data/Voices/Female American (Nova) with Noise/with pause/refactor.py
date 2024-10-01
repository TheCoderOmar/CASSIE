import os

# Specify the directory containing the files
directory = 'Data/Voices/Male British (Oliver)/with pause'

# Loop through the files in the directory
for filename in os.listdir(directory):
    # Check if there's a space in the filename
    if ' ' in filename:
        # Create the new filename by replacing spaces with underscores
        new_filename = filename.replace(' ', '_')
        
        # Get the full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')
