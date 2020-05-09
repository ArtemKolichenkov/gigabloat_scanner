# pylint: disable=W0612,W0613
from .test_utils import get_directory


def check_directory(dir_to_check, expected):
    assert dir_to_check.path == expected.path
    assert dir_to_check.name == expected.name
    assert dir_to_check.file_count == expected.file_count
    assert dir_to_check.subdir_count == expected.subdir_count
    assert dir_to_check.size == expected.size
    assert dir_to_check.hr_size == expected.hr_size
    assert dir_to_check.filetypes == expected.filetypes
    assert dir_to_check.categories == expected.categories


def test_dir_root(remove_ds_stores, scan_result, expected_root):
    root = scan_result.root_directory
    check_directory(root, expected_root)


def test_audio_dir(remove_ds_stores, scan_result, expected_root):
    root = scan_result.root_directory
    audio = get_directory("Audio", root.subdirectories)
    expected_audio = get_directory("Audio", expected_root.subdirectories)
    check_directory(audio, expected_audio)


def test_video_dir(remove_ds_stores, scan_result, expected_root):
    root = scan_result.root_directory
    video = get_directory("Video", root.subdirectories)
    expected_video = get_directory("Video", expected_root.subdirectories)
    check_directory(video, expected_video)


def test_images_dir(remove_ds_stores, scan_result, expected_root):
    root = scan_result.root_directory
    images = get_directory("Images", root.subdirectories)
    expected_images = get_directory("Images", expected_root.subdirectories)
    check_directory(images, expected_images)

    png = get_directory("png", images.subdirectories)
    expected_png = get_directory("png", expected_images.subdirectories)
    check_directory(png, expected_png)

    svg = get_directory("svg", images.subdirectories)
    expected_svg = get_directory("svg", expected_images.subdirectories)
    check_directory(svg, expected_svg)

    # 2. Check files in correct folders
    # 2.1 Check file data is correct

    # This is about Scanner object, not directories
    # assert scan_result.file_count == expected.file_count
    # assert scan_result.dir_count == expected.dir_count
    # assert scan_result.size == expected.size
    # assert scan_result.hr_size == expected.hr_size
