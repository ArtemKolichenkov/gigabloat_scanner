# pylint: disable=W0612,W0613
from .test_utils import get_directory, get_file


def check_file(file, expected):
    assert file.path == expected.path
    assert file.directory.path == expected.directory.path
    assert file.name == expected.name
    assert file.size == expected.size
    assert file.hr_size == expected.hr_size
    assert file.filetype == expected.filetype
    assert file.category == expected.category


def test_files_root(remove_ds_stores, scan_result, expected_root):
    root = scan_result.root_directory
    root_files = root.files
    assert len(root_files) == len(expected_root.files)
    for file in root_files:
        expected_file = get_file(file.path, expected_root.files)
        check_file(file, expected_file)


def test_files_audio(remove_ds_stores, scan_result, expected_root):
    root = scan_result.root_directory
    audio = get_directory("Audio", root.subdirectories)
    expected_audio = get_directory("Audio", expected_root.subdirectories)
    audio_files = audio.files
    assert len(audio_files) == len(expected_audio.files)
    for file in audio_files:
        expected_file = get_file(file.path, expected_audio.files)
        check_file(file, expected_file)


def test_files_video(remove_ds_stores, scan_result, expected_root):
    root = scan_result.root_directory
    video = get_directory("Video", root.subdirectories)
    expected_video = get_directory("Video", expected_root.subdirectories)
    video_files = video.files
    assert len(video_files) == len(expected_video.files)
    for file in video_files:
        expected_file = get_file(file.path, expected_video.files)
        check_file(file, expected_file)


def test_files_images(remove_ds_stores, scan_result, expected_root):
    root = scan_result.root_directory
    images = get_directory("Images", root.subdirectories)
    png = get_directory("png", images.subdirectories)
    svg = get_directory("svg", images.subdirectories)
    expected_images = get_directory("Images", expected_root.subdirectories)
    expected_png = get_directory("png", expected_images.subdirectories)
    expected_svg = get_directory("svg", expected_images.subdirectories)
    png_files = png.files
    svg_files = svg.files
    assert len(png_files) == len(expected_png.files)
    for file in png_files:
        expected_file = get_file(file.path, expected_png.files)
        check_file(file, expected_file)
    for file in svg_files:
        expected_file = get_file(file.path, expected_svg.files)
        check_file(file, expected_file)
