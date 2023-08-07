import os 
from pathlib import Path




class FileControl():


    @staticmethod
    def check_exist(path: Path) -> bool:
        return os.path.exists(path)


    @staticmethod
    def is_file(path: Path) -> bool:
        return os.path.isfile(path)


    @staticmethod
    def is_dir(path: Path) -> bool:
        return os.path.isdir(path)


    @classmethod
    def is_xlsx(cls, path: Path) -> bool:
        extension = cls.get_file_name_extension(path)

        if extension == 'xlsx' or extension == 'xls':
            return True
        
        return False


    @classmethod
    def compare_extension(cls, path: Path, extension_str: str) -> bool:
        """
        if extension_str equals to .extension => True

        else Flase
        """

        extension =  cls.get_file_name_extension(path)

        if extension == extension_str:
            return True
        
        return False

    @staticmethod
    def get_current_path() -> Path:
        return Path(os.getcwd())


    @staticmethod
    def make_dir(path: Path, dir_name: str) -> None:
        new_dir_path = str(path) + '\\' + dir_name
        os.makedirs(new_dir_path, exist_ok=True)


    @staticmethod
    def get_file_name_with_extension(file_path: Path) -> str | None: 
        """
        C:\\Users\\user\\Desktop\\dir\\file.txt

        =>file.txt
        """
        return os.path.basename(file_path) 


    @staticmethod
    def get_file_name_without_extension(file_path: Path) -> str | None:
        """
        C:\\Users\\user\\Desktop\\dir\\text.txt
        
        =>file"""
        return os.path.splitext(os.path.basename(file_path))[0] 


    @staticmethod
    def get_file_name_extension(file_path: Path) -> str | None:
        """
        C:\\Users\\user\\Desktop\\dir\\text.txt

        =>txt
        """
        return os.path.splitext(os.path.basename(file_path))[-1][1:]


    @staticmethod
    def get_pardir_path(file_path: Path) -> Path | None:
        """
        C:\\Users\\user\\Desktop\\dir\\text.txt

        => C:\\Users\\user\\Desktop\\dir
        """
        path_parent = file_path.parent.absolute()

        if os.path.isdir(path_parent):
            return path_parent
        
        return 


    @staticmethod
    def get_pardir_name(file_path: Path) -> str | None:
        """
        C:\\Users\\user\\Desktop\\dir\\text.txt

        => dir
        """

        path_parent = file_path.parent.absolute()

        if os.path.isdir(path_parent):
            return os.path.basename(path_parent)
        
        return




if __name__ == '__main__':
    file_path = str(FileControl.get_current_path()) + r'\test.txt'
    print(FileControl.get_file_name_extension(file_path))
    print(FileControl.get_pardir_name(Path(file_path)))
    print(FileControl.is_file(file_path))