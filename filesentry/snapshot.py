import json
import os
from filesentry.monitor import compute_file_hash

def create_snapshot(directory):
    snapshot = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            try:
                snapshot[path] = compute_file_hash(path)
            except:
                snapshot[path] = "ERROR"
    return snapshot

def save_snapshot(snapshot, path="snapshot.json"):
    with open(path, "w") as f:
        json.dump(snapshot, f)

def load_snapshot(path="snapshot.json"):
    with open(path, "r") as f:
        return json.load(f)
