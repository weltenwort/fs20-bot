# fs20-bot

:warning: This is has not been tested. It will probably not work.

This is the attempt at creating a scaffolding for a bot that reacts to FS20
messages it receives via the serial port.

## Requirements

You can install the requirements using `pip install -r requirements.txt`.

* `pyserial`

## Tools

### `monitor.py`: bus monitor for debugging

Run the tool using `python monitor.py`. It loops until it recives a keyboard
interrupt signal (usually `ctrl-c`) or crashes.
