
def get_directory(dir_name, dir_list):
    for dir_object in dir_list:
        if dir_object.name == dir_name:
            return dir_object
    raise Exception(f"No directory named {dir_name}")


def get_file(filepath, file_list):
    for file_object in file_list:
        if file_object.path == filepath:
            return file_object
    raise Exception(f"No file named {filepath}")
