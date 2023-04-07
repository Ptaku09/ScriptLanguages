import json
import os
import sys
import tarfile
from datetime import datetime


def archive_dir(path):
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
        dirname = os.path.basename(path)
        filename = f"{timestamp}-{dirname}.tar.gz"

        with tarfile.open(filename, "w:gz") as tar:
            tar.add(path, arcname=os.path.basename(path))

        move_archive_to_backups_dir(filename)
        add_entry_to_history_file(timestamp, path, filename)
    except FileNotFoundError:
        print("Invalid path - directory does not exist")


def move_archive_to_backups_dir(filename):
    # check if BACKUPS_DIR env variable is set
    backups_dir = os.environ.get("BACKUPS_DIR") or os.path.expanduser("~/.backups")
    # create backups dir if not exists
    os.makedirs(backups_dir, exist_ok=True)

    # move archive to backups dir
    backup_path = os.path.join(backups_dir, filename)
    os.rename(filename, backup_path)

    return backups_dir


def add_entry_to_history_file(timestamp, path, filename):
    history_dir = os.environ.get("BACKUPS_DIR") or os.path.expanduser("~/.backups")
    history_path = os.path.join(history_dir, "history.json")
    backup_info = {"timestamp": timestamp, "path": path, "filename": filename}

    # read history file if exists
    if os.path.exists(history_path):
        with open(history_path, "r") as f:
            history = json.load(f)
    else:
        history = []

    # append new backup info
    history.append(backup_info)

    # save history file
    with open(history_path, "w") as f:
        json.dump(history, f)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        archive_dir(sys.argv[1])
    else:
        print('Invalid number of arguments, provide path to directory')
