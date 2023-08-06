from pathlib import Path

from FileControl import FileControl as fc


if __name__ == '__main__':
    file_path = str(fc.get_current_path()) + r'\test.txt'
    print(fc.get_file_name_extension(file_path))
    print(fc.get_pardir_name(Path(file_path)))
    print(fc.is_file(file_path))