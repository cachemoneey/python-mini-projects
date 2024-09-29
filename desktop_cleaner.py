import os
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    """Creates a subfolder in the specified path if it doesn't already exist."""
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def move_file_to_subfolder(file_path, subfolder_path):
    """Moves a file to the specified subfolder."""
    shutil.move(file_path, subfolder_path)

def clean_folder(folder_path):
    # Google os library documentation, os.listdir lists all the files in the folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # We are splitting the file name by the dot because the type comes after the dot, then -1 the last index will give us the file extension in lower case 
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                # sort these files into a new folder
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                # moves file into subfolder
                move_file_to_subfolder(file_path, subfolder_path)
                print(f"Moved: {filename} -> {subfolder_name}/")

if __name__ == "__main__":
    print("Desktop Cleaner Script")
    folder_path = 'EDIT THIS' # Choose your desired folder path location
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning complete.")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again.")