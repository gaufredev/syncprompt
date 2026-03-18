# SyncPrompt

A browser-based teleprompter with real-time voice synchronization. Your script scrolls automatically as you speak — no foot pedal, no remote, just your voice.

## Setup (Mac)

**You don't need to install anything.** Everything you need is already on your Mac.

### Step 1 — Download

Download this folder (green **Code** button → **Download ZIP**), then unzip it.

### Step 2 — Allow the start script

Open **Terminal** (search "Terminal" in Spotlight), then drag `start.sh` into the Terminal window. It will paste the file path for you. Press Enter.

> **First time only:** if you get a "permission denied" error, type this in Terminal first, then try again:
> ```
> chmod +x start.sh
> ```

### Step 3 — Done

The app opens automatically in your browser. That's it!

> **Why does this need Terminal?** The microphone only works when the page is served from a local server (a browser security rule). The script starts a tiny server on your Mac — nothing is sent to the internet.

## How to Use

1. **Paste your script** into the editor (left panel)
2. Click **Start** and allow microphone access when your browser asks
3. **Speak naturally** — the prompter follows your voice in real-time
4. Use the **speed** and **font size** controls to adjust to your comfort

### Script Formatting

- `---` or `## Chapter Title` → chapter breaks
- `**bold text**` → emphasis
- Lines starting with `@` → speaker mentions
- Lines in parentheses like `(tone: serious)` → stage directions (ignored by voice matching)

## Troubleshooting

| Problem | Fix |
|---|---|
| "permission denied" when running start.sh | Run `chmod +x start.sh` in Terminal first |
| Browser doesn't open | Go to **http://localhost:8080/syncprompt.html** manually in Chrome |
| Mic not working | Click the lock/settings icon in the address bar → allow microphone |
| Voice sync feels off | Speak closer to the mic, or use Chrome instead of Safari |
| "address already in use" | Another app uses port 8080. Edit `PORT = 8080` in `server.py` to 8081 |

## Notion Edition

There's also a **Notion-connected version** (`syncprompt-notion.html`) that loads scripts directly from a Notion database — no copy-pasting needed. You manage your scripts in Notion and the prompter pulls them in automatically.

This version **only works locally** (not from the hosted GitHub Pages link) because it needs a small server to talk to the Notion API. To use it:

1. Follow the local setup steps above (download + `start.sh`)
2. Open `http://localhost:8080/syncprompt-notion.html` in your browser
3. Enter your Notion API key and database ID in the settings panel

## Recommended Browser

**Google Chrome** works best. Safari works too but voice recognition can be less reliable.

## License

MIT
