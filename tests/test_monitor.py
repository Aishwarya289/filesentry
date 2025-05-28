import sys
import os
sys.path.append(os.path.abspath("."))  # Adds the project root to the module search path

from filesentry import monitor  # Now it will work after adding __init__.py

import tempfile

def test_compute_file_hash():
    # Create a temporary file and write content to it
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(b'hello world')
        temp_path = temp.name

    # Get the hash of the temp file
    result = monitor.compute_file_hash(temp_path)

    # Ensure it's a valid hex string
    assert isinstance(result, str)
    assert len(result) == 64  # SHA-256 hash length

    # Clean up
    os.remove(temp_path)
