""" 
This script creates a _SCROLLS.md file in each subfolder of the SCROLLS_FOLDER if it does not already exist. The _SCROLLS.md file is created with a header line containing the folder name. The script is designed to be run after creating a new subfolder in the SCROLLS_FOLDER to ensure that each subfolder has a corresponding _SCROLLS.md file.
"""

import os

def check_and_create_scrolls(base_folder):
    for root, dirs, files in os.walk(base_folder):
        for subfolder in dirs:
            subfolder_path = os.path.join(root, subfolder)
            # Construct the expected filename
            scroll_file = f"{subfolder}_SCROLLS.md"
            scroll_file_path = os.path.join(subfolder_path, scroll_file)
            
            # Check if the file exists
            if not os.path.exists(scroll_file_path):
                # Create the file if it does not exist
                with open(scroll_file_path, 'w') as file:
                    file.write(f"\n# {subfolder} SCROLLS\n")
                print(f"Created: {scroll_file_path}")
            else:
                print(f"Exists: {scroll_file_path}")

# Example usage
base_folder = r"C:/Users/razer/Desktop/walkerrh.github.io/SCROLLS_FOLDER"  # Replace with the path to your folder
check_and_create_scrolls(base_folder)
