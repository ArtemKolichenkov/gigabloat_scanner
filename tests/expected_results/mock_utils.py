import os

# cwd kinda expects that tests are run via makefile
ABS_TESTFILES_DIR = os.path.abspath("tests/test_files")


class MockDirectory:
    def __init__(self, blueprint):
        self.path = blueprint["path"]
        self.name = blueprint["name"]
        self.parent_dir = None
        self.files = []
        self.file_count = blueprint["file_count"]
        self.subdirectories = None
        self.subdir_count = blueprint["subdir_count"]
        self.size = blueprint["size"]
        self.hr_size = blueprint["hr_size"]
        self.filetypes = blueprint["filetypes"]
        self.categories = blueprint["categories"]

    def add_files(self, files):
        """Since we need reference to dir in files we can't do it in init"""
        self.files = files

    def add_subdirs(self, subdirs):
        self.subdirectories = subdirs

    def add_parent(self, parent):
        self.parent_dir = parent


class MockFile:
    def __init__(self, blueprint):
        self.path = blueprint["path"]
        self.directory = blueprint["directory"]
        self.name = blueprint["name"]
        self.size = blueprint["size"]
        self.hr_size = blueprint["hr_size"]
        self.filetype = blueprint["filetype"]
        self.category = blueprint["category"]
