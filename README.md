## Smart Home Assistant

A simple Python-based smart home assistant that works with both **voice** and **text commands**.

You can control simulated devices in a house, like doors, windows, and lights. The assistant responds with speech and keeps track of the house state.

---

### Features

- Control via **voice** or **text**
- Actions: open/close doors and windows, turn lights on/off
- Voice responses using text-to-speech
- Simulated home state (can be expanded for real hardware)
- Modular and easy to extend

---

### Requirements

```bash
pip install -r requirements.txt
```

Dependencies include:

- `speechrecognition`
- `pyttsx3`
- `pyaudio` *(may require `portaudio` installation on macOS)*

---

### How to Run

```bash
python assistant.py
```

Choose between `voice` or `text` mode when prompted, and start giving commands.

---

### Example Commands

- `open front door`
- `close bedroom window`
- `turn on kitchen light`
- `turn off bedroom light`
- `house status`

---

### Project Structure

```
smart_home_assistant/
├── assistant.py       # Main interface (voice/text)
├── controller.py      # Command handling logic
├── house.py           # Simulated smart home logic
├── config.py          # (Optional future settings)
└── requirements.txt   # Dependencies
```

---

### Future Ideas

- Integration with physical devices (e.g. Raspberry Pi + relays)
- Web interface or mobile app
- Connection to external APIs (e.g. weather, calendar)
- AI-based command understanding (e.g. GPT integration)
