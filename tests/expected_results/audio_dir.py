from .mock_utils import MockDirectory, MockFile, ABS_TESTFILES_DIR


def get_audio_dir():
    audio = MockDirectory(
        {
            "path": ABS_TESTFILES_DIR + "/Audio",
            "name": "Audio",
            "parentDirectory": "ROOT",
            "file_count": 2,
            "subdirectories": None,
            "subdir_count": 0,
            "size": 1837394,
            "hr_size": "1.8 MB",
            "filetypes": {
                ".mp3": 1,
                ".wav": 1
            },
            "categories": {
                "audio": 2
            }
        }
    )

    mp3_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Audio/example_MP3.mp3",
            "directory": audio,
            "name": "example_MP3.mp3",
            "size": 764176,
            "hr_size": "764.2 kB",
            "filetype": ".mp3",
            "category": "audio"
        }
    )

    wav_file = MockFile(
        {
            "path": ABS_TESTFILES_DIR + "/Audio/example_WAV.wav",
            "directory": audio,
            "name": "example_WAV.wav",
            "size": 1073218,
            "hr_size": "1.1 MB",
            "filetype": ".wav",
            "category": "audio"
        }
    )

    audio.add_files([mp3_file, wav_file])
    return audio
