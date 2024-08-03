""" 
This script adds a comment with the file path to the top of each file in the SCROLLS_FOLDER.
"""


import os

# Base path to the SCROLLS_FOLDER
base_path = r'C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER'

# Function to determine the comment style based on file extension
def get_comment_style(file_path):
    _, ext = os.path.splitext(file_path)
    if ext in ['.py', '.sh', '.pl', '.rb']:  # Script files
        return "#"
    elif ext in ['.js', '.java', '.c', '.cpp', '.h']:  # C-style languages
        return "//"
    elif ext in ['.html', '.xml']:  # Markup files
        return "<!--", "-->"
    elif ext in ['.md']:  # Markdown files
        return "<!--", "-->"
    else:
        return "#"

# Iterate through all folders and files in the base path
for root, dirs, files in os.walk(base_path):
    for file in files:
        file_path = os.path.join(root, file)
        
        # Read the current content of the file with explicit encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            content_lines = f.readlines()
        
        # Get the comment style for the file type
        comment_start = get_comment_style(file_path)
        if isinstance(comment_start, tuple):  # For markup comments
            comment_start, comment_end = comment_start
            comment = f"{comment_start} {file_path} {comment_end}"
        else:
            comment = f"{comment_start} {file_path}"
        
        # Check for an existing file path comment in the first 5 lines
        found = False
        for i in range(min(5, len(content_lines))):
            if comment_start in content_lines[i] and file_path in content_lines[i]:
                content_lines.pop(i)
                found = True
                break
        
        # Prepare the new content with the comment and two empty lines
        new_content = [f"{comment}\n"] + content_lines
        
        # Write the new content back to the file with explicit encoding
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_content)
        
        print(f"Updated: {file_path}")

print("Script completed.")
