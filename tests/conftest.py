from pathlib import Path
import os
import pytest
from .context import gigabloat
from .expected_results import setup_mocks


PATH_TO_TEST = os.path.abspath("tests/test_files")


@pytest.fixture(scope="function")
def remove_ds_stores():
    stores = Path(PATH_TO_TEST).rglob(".DS_Store")
    for store_file in stores:
        os.remove(store_file)
    yield


@pytest.fixture(scope="function")
def scan_result():
    empty_dir = PATH_TO_TEST + "/EmptyDir"
    if not os.path.isdir(empty_dir):
        os.makedirs(empty_dir)
    test_scanner = gigabloat.Scanner(PATH_TO_TEST)
    test_scanner.full_scan()
    return test_scanner


@pytest.fixture(scope="function")
def expected_root():
    root = setup_mocks()
    return root
