import os

# Path to the SCROLLS_FOLDER
base_path = r'C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER'

# Function to add files and nested scrolls files within the folder
def add_files_and_scrolls(folder_path, base_path, parent_filename):
    filename = f"{os.path.basename(folder_path)}_SCROLLS.md"
    filepath = os.path.join(folder_path, filename)

    # Check if the _SCROLLS.md file exists
    if os.path.exists(filepath):
        # Read the current content of the _SCROLLS.md file
        with open(filepath, 'r', encoding='utf-8') as scrolls_file:
            scrolls_content = scrolls_file.readlines()

        # Find the last line with text and remove existing "### Files in this folder:" section
        new_content = []
        last_text_line_index = -1
        inside_files_section = False
        for i, line in enumerate(scrolls_content):
            if line.strip():
                last_text_line_index = i
            if line.strip() == "### Files in this folder:":
                inside_files_section = True
                continue
            if inside_files_section:
                if line.startswith("- ["):
                    continue
                else:
                    inside_files_section = False
            new_content.append(line)
        
        # Trim any whitespace or empty lines after the last line of text
        new_content = new_content[:last_text_line_index + 1]

        # Ensure two empty lines before adding new files section
        new_content.append("\n### Files in this folder:\n")

        for f in os.listdir(folder_path):
            file_path = os.path.join(folder_path, f)
            if os.path.isdir(file_path):
                scrolls_file_in_subdir = f"{f}_SCROLLS.md"
                scrolls_file_path = os.path.join(file_path, scrolls_file_in_subdir)
                if os.path.exists(scrolls_file_path):
                    relative_scrolls_path = os.path.relpath(scrolls_file_path, start=base_path).replace("\\", "/")
                    # Convert .md to .html
                    relative_scrolls_path_html = relative_scrolls_path.replace('.md', '.html')
                    new_content.append(f"- [{f.replace('.md', '')}_SCROLLS](/SCROLLS_FOLDER/{relative_scrolls_path_html})\n")
                    # Recursively call to add nested scrolls within the current directory
                    add_files_and_scrolls(file_path, base_path, scrolls_file_in_subdir)
            elif os.path.isfile(file_path) and f != parent_filename:
                relative_path = os.path.relpath(file_path, start=base_path).replace("\\", "/")
                display_name = os.path.splitext(f)[0]  # Remove file extension from display name
                if f.endswith('.md'):
                    relative_path = relative_path.replace('.md', '.html')
                new_content.append(f"- [{display_name.replace('.md', '')}](/SCROLLS_FOLDER/{relative_path})\n")

        # Write the updated content back to the _SCROLLS.md file
        with open(filepath, 'w', encoding='utf-8') as scrolls_file:
            scrolls_file.writelines(new_content)
        
        print(f"Updated: {filepath}")

# Iterate through each folder in the base path and update _SCROLLS.md files
for root, dirs, files in os.walk(base_path):
    for folder in dirs:
        folder_path = os.path.join(root, folder)
        if folder.isupper():
            add_files_and_scrolls(folder_path, base_path, f"{folder}_SCROLLS.md")

print("Script completed.")
