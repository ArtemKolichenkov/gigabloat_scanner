from .mock_utils import MockDirectory, MockFile, ABS_TESTFILES_DIR


def get_video_dir():
    video = MockDirectory(
        {
            "path": ABS_TESTFILES_DIR + "/Video",
            "name": "Video",
            "parentDirectory": "ROOT",
            "file_count": 3,
            "subdirectories": None,
            "subdir_count": 0,
            "size": 3488131,
            "hr_size": "3.5 MB",
            "filetypes": {
                ".avi": 1,
                ".mp4": 1,
                ".wmv": 1
            },
            "categories": {
                "video": 3
            }
        }
    )

    avi_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Video/example_AVI.avi",
            "directory": video,
            "name": "example_AVI.avi",
            "size": 742478,
            "hr_size": "742.5 kB",
            "filetype": ".avi",
            "category": "video"
        }
    )

    mp4_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Video/example_MP4.mp4",
            "directory": video,
            "name": "example_MP4.mp4",
            "size": 1570024,
            "hr_size": "1.6 MB",
            "filetype": ".mp4",
            "category": "video"
        }
    )

    wmv_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Video/example_WMV.wmv",
            "directory": video,
            "name": "example_WMV.wmv",
            "size": 1175629,
            "hr_size": "1.2 MB",
            "filetype": ".wmv",
            "category": "video"
        }
    )

    video.add_files([avi_file, mp4_file, wmv_file])
    return video
