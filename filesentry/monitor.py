# filesentry/monitor.py
import hashlib
import os

def compute_file_hash(path):
    sha = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest()
