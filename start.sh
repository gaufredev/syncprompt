#!/bin/bash
# Start local server for SyncPrompt
# Serves this folder on localhost so the microphone and teleprompter window work

PORT=8080
DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Starting SyncPrompt on http://localhost:$PORT"
echo "Press Ctrl+C to stop"
echo ""

python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$DIR" &
PID=$!

# Open in browser
sleep 0.5
open "http://localhost:$PORT/syncprompt.html"

# Wait for Ctrl+C
trap "kill $PID 2>/dev/null; echo ''; echo 'Server stopped.'; exit 0" INT
wait $PID
