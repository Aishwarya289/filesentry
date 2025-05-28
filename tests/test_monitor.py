import sys
import os
import tempfile

sys.path.append(os.path.abspath("."))  # Ensures project root is in PYTHONPATH

from filesentry import monitor

def test_compute_file_hash():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"test content")
        tmp_path = tmp.name

    try:
        result = monitor.compute_file_hash(tmp_path)

        if not isinstance(result, str):
            raise AssertionError("Result is not a string")
        if len(result) != 64:
            raise AssertionError("Hash length is not 64 characters")
    finally:
        os.remove(tmp_path)
