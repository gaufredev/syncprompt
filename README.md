# SyncPrompt

A browser-based teleprompter with real-time voice synchronization. Your script scrolls automatically as you speak — no foot pedal, no remote, just your voice. It also generates timestamped subtitle files (SRT, VTT) as you record, ready to use in your video editor.

## Try It Online

**No install needed** — open the app directly in your browser:

👉 **https://gaufredev.github.io/syncprompt/syncprompt.html**

Use **Safari** for the best experience (on-device speech recognition, works offline). Chrome and Edge work too but rely on cloud servers. **Firefox probably won't work** (voice sync requires the Web Speech API, which Firefox doesn't support).

## Local Setup (Mac)

If you want to run it locally (needed for the Notion edition), everything you need is already on your Mac.

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

### Multi-Language Support

SyncPrompt automatically detects and switches between languages as you speak (Korean, English, French, and more). For best results:

- **Select the languages** used in your script from the sidebar
- **Keep languages on separate lines** — the system detects the language per line and adjusts voice recognition accordingly
- Mixing two languages on the same line works but is harder for the system to switch

### Script Formatting

- `---` or `## Chapter Title` → chapter breaks
- `**bold text**` → emphasis
- Lines starting with `@` → speaker mentions
- Lines in parentheses like `(tone: serious)` → stage directions (ignored by voice matching)

## Troubleshooting

| Problem | Fix |
|---|---|
| "permission denied" when running start.sh | Run `chmod +x start.sh` in Terminal first |
| Browser doesn't open | Go to **http://localhost:8080/syncprompt.html** manually |
| Mic not working | Click the lock/settings icon in the address bar → allow microphone |
| Voice sync feels off | Speak closer to the mic. On Mac, Safari tends to be more reliable than Chrome |
| "address already in use" | Another app uses port 8080. Edit `PORT = 8080` in `server.py` to 8081 |

## Notion Edition

There's also a **Notion-connected version** (`syncprompt-notion.html`) that loads scripts directly from a Notion database — no copy-pasting needed. You manage your scripts in Notion and the prompter pulls them in automatically.

This version **only works locally** (not from the hosted GitHub Pages link) because it needs a small server to talk to the Notion API. To use it:

1. Follow the local setup steps above (download + `start.sh`)
2. Open `http://localhost:8080/syncprompt-notion.html` in your browser
3. Enter your Notion API key and database ID in the settings panel

## Browser Compatibility

- **Safari (Mac) — Recommended.** Voice recognition runs on-device (Apple Speech), works offline, most reliable.
- **Chrome (Mac/Windows) — Works**, but voice recognition uses Google servers (requires internet). May occasionally go silent during long sessions — the app detects this and auto-recovers.
- **Edge (Windows) — Should work.** Same engine as Chrome, not extensively tested.

## Lighter Code, Faster App, Greener Web

Every website you visit uses energy — from the server that hosts it, through the network that delivers it, to the device that displays it. The average web page loads over 2 MB of data per visit, and the internet's total carbon footprint now rivals the airline industry's.

A lighter app doesn't just help the planet — it loads faster and runs smoother for you. SyncPrompt is built with this in mind:

- **No Google Fonts** — uses your device's built-in fonts instead of downloading ~300 KB of web fonts per visit
- **No heavy frameworks** — pure HTML, CSS, and vanilla JavaScript
- **No tracking scripts** — nothing phoning home in the background
- **No unnecessary images** — even the favicon is a lightweight inline SVG

Curious about the footprint of your own sites? [Website Carbon Calculator](https://www.websitecarbon.com) · [Green Web Foundation](https://www.thegreenwebfoundation.org)

## License

MIT
