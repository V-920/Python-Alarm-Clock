# Python Alarm Clock

A simple command-line alarm clock built using Python. It allows users to set an alarm and plays an audio notification when the specified time is reached.

## Features

- Set an alarm using `HH:MM:SS` format.
- Displays the current time every second.
- Plays an audio notification when the alarm goes off.
- Simple command-line interface.
- Uses Python's built-in time and datetime modules.

## Technologies Used

- **Python**
- `time` – Controls the time intervals.
- `datetime` – Retrieves the current time.
- `playsound` – Plays the alarm sound.

## Project Structure

```text
Python-Alarm-Clock/
│
├── Timer.py
├── sound.wav
└── README.md
```

## Installation & Setup

**1. Clone the repository**

```bash
git clone github.com/V-920/Python-Alarm-Clock
```

**2. Navigate to the project directory**

```bash
cd Python-Alarm-Clock
```

**3. Install the required dependency**

```bash
pip install playsound
```

**4. Run the program**

```bash
python Timer.py
```

## Usage

1. Run the Python script.
2. Enter the alarm time in `HH:MM:SS` format.
3. The program displays the current time.
4. When the specified time is reached, the alarm sound plays.

**Example input:**

```text
Enter the duration of the alarm in seconds (HH:MM:SS): 16:30:00
```

## Requirements

- Python 3.x
- playsound library
- A `sound.wav` audio file in the project directory.

## Future Improvements

- Add the ability to set alarms using durations.
- Allow users to stop the alarm manually.
- Support multiple alarms.
- Improve the command-line interface.

---

Made with Python.
