from .mock_utils import MockDirectory, ABS_TESTFILES_DIR
from .root_dir import get_root_dir
from .video_dir import get_video_dir
from .audio_dir import get_audio_dir
from .images_dir import get_images_dir


def setup_mocks():
    root = get_root_dir()
    empty_dir = MockDirectory(
        {
            "path": ABS_TESTFILES_DIR + "EmptyDir",
            "name": "EmptyDir",
            "parentDirectory": root,
            "files": [],
            "file_count": 0,
            "subdirectories": [],
            "subdir_count": 0,
            "size": 0,
            "hr_size": "0 B",
            "filetypes": {},
            "categories": {}
        }
    )
    audio = get_audio_dir()
    audio.add_parent(root)
    video = get_video_dir()
    video.add_parent(root)
    images = get_images_dir()
    images.add_parent(root)
    root.add_subdirs([audio, video, images, empty_dir])
    return root
