import os
import datetime

def parse_directory(directory_path):
    ignore_files = ['.gitignore']
    ignore_dirs = ['.git']
    total_chars = 0
    files = []  

    for root, dirs, file_names in os.walk(directory_path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file_name in file_names:
            if file_name in ignore_files: 
                continue
            file_path = os.path.join(root, file_name)
            relative_dir = os.path.relpath(root, start=directory_path)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                contents = file.read()
                total_chars += len(contents)

                if len(contents) > 6000:
                    start = 0
                    end = 6000
                    while start < len(contents) and end <= len(contents):
                        while end < len(contents) and contents[end] != '\n':
                            end -= 1
                        end += 1  # Include the newline character in the current part
                        part = contents[start:end].strip()
                        obj = f"``` {relative_dir}/{file_name}.{'continued' if start > 0 else ''}\n{part}\n```\n"
                        files.append(obj)
                        start = end
                        end += 6000
                else:
                    obj = f"``` {relative_dir}/{file_name}\n{contents}\n```\n"
                    files.append(obj)
    print(f"Total number of characters: {total_chars}")
    return files



def write_code_blocks_to_files(code_blocks):
    now = datetime.datetime.now()
    date_string = now.strftime("%d-%m-%Y-%H-%M-%S")

    current_file = ""
    current_file_length = 0
    file_index = 1
    

    for code_block in code_blocks:
        if current_file_length + len(code_block) > 30000:
            filename = f"{date_string}-{file_index}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(current_file)

            current_file = ""
            current_file_length = 0
            file_index += 1

        current_file += code_block
        current_file_length += len(code_block)

    if current_file_length > 0:
        filename = f"{date_string}-{file_index}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(current_file)


if __name__ == '__main__':
    objects = parse_directory('./')
    write_code_blocks_to_files(objects)
