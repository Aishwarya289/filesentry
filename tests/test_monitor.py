from filesentry import monitor
import tempfile
import os

def test_compute_file_hash():
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(b'hello world')
        temp_path = temp.name

    result = monitor.compute_file_hash(temp_path)
    assert isinstance(result, str)
    os.remove(temp_path)
