from .mock_utils import MockDirectory, MockFile, ABS_TESTFILES_DIR


def get_images_dir():
    images = MockDirectory(
        {
            "path": ABS_TESTFILES_DIR + "/Images",
            "name": "Images",
            "parentDirectory": "ROOT",
            "files": [],
            "file_count": 0,
            "subdir_count": 2,
            "size": 15965,
            "hr_size": "16.0 kB",
            "filetypes": {},
            "categories": {}
        }
    )

    png = MockDirectory(
        {
            "path": ABS_TESTFILES_DIR + "/Images/png",
            "name": "png",
            "file_count": 4,
            "subdirectories": [],
            "subdir_count": 0,
            "size": 13500,
            "hr_size": "13.5 kB",
            "filetypes": {
                ".png": 4
            },
            "categories": {
                "image": 4
            }
        }
    )

    apache_png_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Images/png/apache.png",
            "directory": png,
            "name": "apache.png",
            "size": 5251,
            "hr_size": "5.3 kB",
            "filetype": ".png",
            "category": "image"
        }
    )

    apple_png_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Images/png/apple.png",
            "directory": png,
            "name": "apple.png",
            "size": 1381,
            "hr_size": "1.4 kB",
            "filetype": ".png",
            "category": "image"
        }
    )

    ceylon_png_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Images/png/ceylon.png",
            "directory": png,
            "name": "ceylon.png",
            "size": 2818,
            "hr_size": "2.8 kB",
            "filetype": ".png",
            "category": "image"
        }
    )

    yarn_png_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Images/png/yarn.png",
            "directory": png,
            "name": "yarn.png",
            "size": 4050,
            "hr_size": "4.0 kB",
            "filetype": ".png",
            "category": "image"
        }
    )

    png.add_parent(images)
    png.add_files([apache_png_file, apple_png_file, ceylon_png_file, yarn_png_file])

    svg = MockDirectory(
        {
            "path": ABS_TESTFILES_DIR + "/Images/svg",
            "name": "svg",
            "files": ["apple.svg", "yarn.svg"],
            "file_count": 2,
            "subdirectories": [],
            "subdir_count": 0,
            "size": 2465,
            "hr_size": "2.5 kB",
            "filetypes": {
                ".svg": 2
            },
            "categories": {
                "image": 2
            }
        }
    )

    apple_svg_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Images/svg/apple.svg",
            "directory": svg,
            "name": "apple.svg",
            "size": 694,
            "hr_size": "694 Bytes",
            "filetype": ".svg",
            "category": "image"
        }
    )

    yarn_svg_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Images/svg/yarn.svg",
            "directory": svg,
            "name": "yarn.svg",
            "size": 1771,
            "hr_size": "1.8 kB",
            "filetype": ".svg",
            "category": "image"
        }
    )

    svg.add_parent(images)
    svg.add_files([apple_svg_file, yarn_svg_file])

    images.add_subdirs([png, svg])
    return images
