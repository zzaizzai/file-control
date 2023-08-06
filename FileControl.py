import os 
from pathlib import Path


def check_exist(path: Path) -> bool:
    return os.path.exists(path)

def is_file(path: Path) -> bool:
    return os.path.isfile(path)

def is_dir(path: Path) -> bool:
    return os.path.isdir(path)


def get_current_path() -> Path:
    return Path(os.getcwd())


def get_file_name_with_extension(file_path: Path) -> str: 
    """
    C:\\Users\\user\\Desktop\\dir\\file.txt

    =>file.txt
    """
    return os.path.basename(file_path) 

def get_file_name_without_extension(file_path: Path) -> str:
    """
    C:\\Users\\user\\Desktop\\dir\\text.txt
    
    =>file"""
    return os.path.splitext(os.path.basename(file_path))[0] 

def get_file_name_extension(file_path: Path) -> str:
    """
    C:\\Users\\user\\Desktop\\dir\\text.txt

    =>txt
    """
    return os.path.splitext(os.path.basename(file_path))[-1][1:]

def get_pardir_path(file_path: Path) -> Path:
    """
    C:\\Users\\user\\Desktop\\dir\\text.txt

    => C:\\Users\\user\\Desktop\\dir
    """
    path_parent = file_path.parent.absolute()

    if os.path.isdir(path_parent):
        return path_parent
    
    return 

def get_pardir_name(file_path: Path) -> str:
    """
    C:\\Users\\user\\Desktop\\dir\\text.txt

    => dir
    """

    path_parent = file_path.parent.absolute()

    if os.path.isdir(path_parent):
        return os.path.basename(path_parent)
    
    return


if __name__ == '__main__':
    file_path = str(get_current_path()) + r'\test.txt'
    print(get_file_name_extension(file_path))
    print(get_pardir_name(Path(file_path)))
    print(is_file(file_path))