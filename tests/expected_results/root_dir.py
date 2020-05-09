from .mock_utils import MockDirectory, MockFile, ABS_TESTFILES_DIR


def get_root_dir():
    root = MockDirectory(
        {
            "path": ABS_TESTFILES_DIR,
            "name": "test_files",
            "parentDirectory": None,
            "file_count": 3,
            "subdir_count": 4,
            "size": 5342949,
            "hr_size": "5.3 MB",
            "filetypes": {
                ".png": 1,
                ".json": 1,
                ".txt": 1
            },
            "categories": {
                "image": 1,
                "document": 1,
                "other": 1
            }
        }
    )

    example_png_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/example.png",
            "directory": root,
            "name": "example.png",
            "size": 1381,
            "hr_size": "1.4 kB",
            "filetype": ".png",
            "category": "image"
        }
    )

    example_json_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/example.json",
            "directory": root,
            "name": "example.json",
            "size": 48,
            "hr_size": "48 Bytes",
            "filetype": ".json",
            "category": "other"
        }
    )

    example_txt_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/example.txt",
            "directory": root,
            "name": "example.txt",
            "size": 30,
            "hr_size": "30 Bytes",
            "filetype": ".txt",
            "category": "document"
        }
    )

    root.add_files([example_png_file, example_json_file, example_txt_file])
    return root
