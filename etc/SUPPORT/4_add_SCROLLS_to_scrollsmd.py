""" 
This script is used to append the paths of the _SCROLLS.md files in the first level of the folder C:\\Users\\razer\\Desktop\\walkerrh.github.io\\SCROLLS_FOLDER to the C:\\\\Users\\\\razer\\\\Desktop\\\\walkerrh.github.io\\\\SCROLLS_FOLDER\\\\scrolls.md file.
"""


import os

def append_scrolls_paths_to_main_scrolls(folder_path, main_scrolls_path):
    # Clear the content of the main scrolls file and add a comment with the folder path
    with open(main_scrolls_path, 'w', encoding='utf-8') as main_scrolls_file:
        main_scrolls_file.write(f"<!-- Folder path: {folder_path} -->\n\n")

    # Open the main scrolls file in append mode
    with open(main_scrolls_path, 'a', encoding='utf-8') as main_scrolls_file:
        # List the items in the folder path
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path) and item.endswith('_SCROLLS.md'):
                # Get the full path of the scroll file
                scroll_file_path = os.path.join(folder_path, item)
                # Generate the markdown path
                relative_path = os.path.relpath(scroll_file_path, folder_path).replace("\\", "/")
                markdown_path = f" [{item.replace('.md', '')}](/SCROLLS_FOLDER/{relative_path.replace('.md', '.html')})"
                # Append the markdown path to the main scrolls file
                main_scrolls_file.write(f"\n{markdown_path}\n")
            elif os.path.isdir(item_path):
                for file in os.listdir(item_path):
                    file_path = os.path.join(item_path, file)
                    if os.path.isfile(file_path) and file.endswith('_SCROLLS.md'):
                        # Get the full path of the scroll file
                        scroll_file_path = file_path
                        # Generate the markdown path
                        relative_path = os.path.relpath(scroll_file_path, folder_path).replace("\\", "/")
                        markdown_path = f" [{file.replace('.md', '')}](/SCROLLS_FOLDER/{relative_path.replace('.md', '.html')})"
                        # Append the markdown path to the main scrolls file
                        main_scrolls_file.write(f"\n{markdown_path}\n")

if __name__ == "__main__":
    folder_path = "C:\\Users\\razer\\Desktop\\walkerrh.github.io\\SCROLLS_FOLDER"
    main_scrolls_path = os.path.join(folder_path, "scrolls.md")
    append_scrolls_paths_to_main_scrolls(folder_path, main_scrolls_path)
