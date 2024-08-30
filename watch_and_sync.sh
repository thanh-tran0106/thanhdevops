#!/bin/bash

# Directory to watch
WATCH_DIR="/home/ubuntu/thanhdevops/media/cats_photos/"

# Remote server details
REMOTE_USER="ubuntu"
REMOTE_HOST="172.31.45.204"
REMOTE_DIR="/home/ubuntu/media/cats_photos/"

# Watch the directory for changes
inotifywait -m -r -e create,move,delete,modify --format '%w%f' "${WATCH_DIR}" | while read FILE
do
    # Sync the changes to the remote server
    rsync -avz "${WATCH_DIR}" "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_DIR}"
done
