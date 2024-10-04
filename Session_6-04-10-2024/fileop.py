def open_file(file_path, mode):
    try:
        file = open(file_path, mode)
        return file
    except IOError as e:
        print(f"Error opening file: {e}")
        return None

def close_file(file):
    try:
        file.close()
    except IOError as e:
        print(f"Error closing file: {e}")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing to file: {e}")

def append_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
    except IOError as e:
        print(f"Error appending to file: {e}")

def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
    except IOError as e:
        print(f"Error copying file: {e}")

source_file_path = 'source.txt'
destination_file_path = 'destination.txt'


write_file(source_file_path, "Hello, World!\n")


append_file(source_file_path, "Appending some text.\n")


content = read_file(source_file_path)
print("Content of source file:")
print(content)

copy_file(source_file_path, destination_file_path)

copied_content = read_file(destination_file_path)
print("Content of destination file:")
print(copied_content)