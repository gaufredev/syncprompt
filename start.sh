#!/bin/bash
# Start local server for SyncPrompt
# Uses server.py for Notion API proxy + static file serving

DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Starting SyncPrompt on http://localhost:8080"
echo "Press Ctrl+C to stop"
echo ""

cd "$DIR"
python3 "$DIR/server.py" &
PID=$!

# Open in browser
sleep 0.5
open "http://localhost:8080/syncprompt-notion.html"

# Wait for Ctrl+C
trap "kill $PID 2>/dev/null; echo ''; echo 'Server stopped.'; exit 0" INT
wait $PID
