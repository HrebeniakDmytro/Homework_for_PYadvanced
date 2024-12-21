from typing import List, Optional

class File:
    def __init__(self, name: str, directory: Optional['Directory'] = None):
        self.name: str = name
        self.directory: Optional[Directory] = directory

class Directory:
    def __init__(self, name: str, root: Optional['Directory'] = None):
        self.name: str = name
        self.root: Optional[Directory] = root
        self.files: List[File] = []
        self.sub_directories: List['Directory'] = []

    def add_sub_directory(self, sub_directory: 'Directory') -> None:
        sub_directory.root = self
        self.sub_directories.append(sub_directory)

    def remove_sub_directory(self, sub_directory: 'Directory') -> None:
        if sub_directory in self.sub_directories:
            sub_directory.root = None
            self.sub_directories.remove(sub_directory)

    def add_file(self, file: File) -> None:
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File) -> None:
        if file in self.files:
            file.directory = None
            self.files.remove(file)
