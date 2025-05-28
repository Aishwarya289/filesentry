import os
import tempfile
from filesentry import monitor


def test_calculate_file_hash():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"test content")
        tmp_path = tmp.name

    try:
        # Call the function
        result = monitor.calculate_file_hash(tmp_path)

        # Ensure it's a valid hex string of SHA-256 length
        if not isinstance(result, str):
            raise AssertionError("Result is not a string")
        if len(result) != 64:
            raise AssertionError("Hash length is not 64 characters")
    finally:
        os.remove(tmp_path)


def test_monitor_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "testfile.txt")
        with open(file_path, "w") as f:
            f.write("initial content")

        # Run the monitor function once
        file_hashes = monitor.monitor_directory(temp_dir, run_once=True)

        # Check if the file was detected
        if file_path not in file_hashes:
            raise AssertionError("Monitored file not detected")
