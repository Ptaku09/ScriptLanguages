import json
import os
import sys
import tarfile


def restore_backup(path):
    try:
        backups_dir = os.environ.get("BACKUPS_DIR") or os.path.expanduser("~/.backups")
        backup = pick_backup(backups_dir)

        # remove all files from directory
        clear_dir(path)

        # Extract backup
        with tarfile.open(os.path.join(backups_dir, backup['filename']), 'r:gz') as tar:
            tar.extractall(path)

        print('Backup restored successfully')
    except FileNotFoundError:
        print('Invalid path - directory does not exist')


def pick_backup(backups_dir):
    history_file = os.path.join(backups_dir, 'history.json')

    if not os.path.exists(history_file):
        print('History file not found')
        sys.exit(1)

    with open(history_file) as f:
        history = json.load(f)

    print('Available backups:')
    for i, backup in enumerate(reversed(history)):
        print(f"{i + 1}. {backup['timestamp']} - {backup['path']} - {backup['filename']}")

    while True:
        try:
            choice = int(input('Choose backup to restore: '))
            backup = history[-choice]
            break
        except (ValueError, IndexError):
            print('Wrong backup number. Try again.')

    return backup


def clear_dir(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        restore_backup(sys.argv[1])
    else:
        restore_backup(os.getcwd())
