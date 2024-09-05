# Keylogger Project

This project contains a keylogger that logs keystrokes and sends them to a logging server. The keylogger is implemented in [keylogger.py](./keylogger.py) and uses a remote logging server to store the recorded keystrokes. The logging server is located in the subdirectory [/logging-server/](./logging-server/).

## Important Notes

- **The keylogger is to be used exclusively for educational, ethical, and legal purposes!**
- **The author assumes no responsibility for damages resulting from improper or unethical use of this tool.**
- **Please ensure that you have the consent of all affected individuals before using the keylogger.**

## Prerequisites

Before starting the keylogger, make sure the logging server is properly set up and operational. Instructions for this can be found in the file [README.md](./logging-server/README.md).

## Installation

> **NOTE:** Ensure that Python 3.1x or higher is installed before running the keylogger. It is also recommended to create a virtual environment to manage the project's dependencies.

1. Create a virtual environment:

   ```bash
   call activate-venv.bat
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Keylogger

> **NOTE:** Before starting, please ensure that the logging server is correctly set up and operational before running the keylogger.

The keylogger can be started by running the `keylogger.py` script:

```bash
python keylogger.py
```

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more details.
