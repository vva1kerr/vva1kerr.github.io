import os
import re

def sanitize_filename(filepath):
    """
    Given a file path, sanitize the filename to be web hosting compatible.
    This includes removing a variety of special characters and replacing whitespace with underscores.
    
    Args:
        filepath (str): The original file path.
    
    Returns:
        str: The sanitized file path.
    """
    directory, filename = os.path.split(filepath)
    name, ext = os.path.splitext(filename)
    
    # Define characters to be removed
    special_chars = '.,:;\'"“”><()\/][}{+-=*&^%$#@!'
    
    # Remove special characters and replace whitespace with underscores
    sanitized_name = re.sub(f'[{re.escape(special_chars)}]', '', name).replace(" ", "_")
    
    # Reassemble the sanitized filename
    sanitized_filename = sanitized_name + ext
    
    # Reconstruct the full file path
    sanitized_filepath = os.path.join(directory, sanitized_filename)
    
    return sanitized_filepath

def rename_file(filepath):
    """
    Rename the file at the given file path to its sanitized version.
    
    Args:
        filepath (str): The original file path.
    
    Returns:
        str: The new sanitized file path.
    """
    sanitized_filepath = sanitize_filename(filepath)
    
    # Rename the file
    os.rename(filepath, sanitized_filepath)
    
    return sanitized_filepath

# def rename_files_in_folder(folder_path):
#     """
#     Rename all files in the given folder to their sanitized versions.
    
#     Args:
#         folder_path (str): The path to the folder containing files to be renamed.
#     """
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#         if os.path.isfile(file_path):
#             sanitized_path = rename_file(file_path)
#             print(f"Renamed: {file_path} -> {sanitized_path}")

# Example usage
original_path = r"C:\Users\razer\Desktop\walkerrh.github.io\assets\art\Sacrifice_of_Abraham_and_the_Adoration_of_the_Magi_Georgios_Klontzas_16th_century.png"
sanitized_path = rename_file(original_path)
print("Original Path:", original_path)
print("Sanitized Path:", sanitized_path)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # Example usage
# folder_path = r"C:\Users\razer\Desktop\walkerrh.github.io\assets\art"
# rename_files_in_folder(folder_path)