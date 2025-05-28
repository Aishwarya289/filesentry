from filesentry.snapshot import create_snapshot, save_snapshot, load_snapshot
from filesentry.alert import alert
import os
import sys

def compare_snapshots(old, new):
    for path in new:
        if path not in old:
            alert(f"New file detected: {path}")
        elif new[path] != old[path]:
            alert(f"File modified: {path}")
    for path in old:
        if path not in new:
            alert(f"File deleted: {path}")

def run_monitor(directory):
    if not os.path.exists("snapshot.json"):
        print("No snapshot found. Creating new snapshot...")
        snapshot = create_snapshot(directory)
        save_snapshot(snapshot)
        print("Snapshot created.")
    else:
        old_snapshot = load_snapshot()
        new_snapshot = create_snapshot(directory)
        compare_snapshots(old_snapshot, new_snapshot)
        save_snapshot(new_snapshot)
        print("Snapshot updated.")

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "sample_dir"
    run_monitor(target_dir)
