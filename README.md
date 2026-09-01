# simplog

A lightweight, portable, and simple terminal logging library designed for Python beginners.

simplog ditches the complex configuration of Python's built-in logging module and gives you exactly what you need to debug your code in the terminal right now.

## Features
* 🚀 Zero Configuration: Just import and start logging.
* 📦 Ultra-lightweight: Under 100 lines of clean code.
* 🔢 5 Log Levels: DEBUG, INFO, WARNING, ERROR, and FATAL.
* 💾 Optional File Logging: Mirror your logs to a local file with a single parameter.

## Installation

You can install `simplog` directly from this GitHub repository using `pip`:

```bash
pip install git+https://github.com/luka-mladjenovic/simplog.git
```

To install a specific version:

```bash
pip install git+https://github.com/luka-mladjenovic/simplog.git@v0.2.0
```

## Quick Start Guide

Using simplog is very straightforward. Here is how you can get started in less than a minute:

```python
from simplog import SimpLog
```

### Initialize the logger
The first argument is a name that identifies this logger — useful when logging across multiple files. The default level is `"INFO"`.
```python
logger = SimpLog("main.py")
```

### Log messages based on severity
```python
logger.info("Application started successfully.")

logger.warn("Configuration file missing. Using defaults.")

logger.error("Could not connect to the database.")

logger.fatal("System crashed! Exiting application.")
```

### This DEBUG message will NOT print because our level is set to INFO
```python
logger.debug("This is a hidden developer message.")
```

---

### Persistent File Logging

Pass a `file_path` to mirror all filtered terminal output into a local text file. Logs are appended across runs, so your history is never overwritten.

```python
logger = SimpLog("main.py", level="DEBUG", file_path="app.log")

logger.info("This prints to the terminal and is saved to app.log.")
```

---

### Log Level Thresholds

simplog filters out messages that are lower priority than the level you set during initialization. The hierarchy from lowest to highest is:

1. DEBUG (Lowest - used for step-by-step developer troubleshooting)
2. INFO (General confirmation messages of normal operation)
3. WARNING (An indication that something unexpected happened, or a problem is coming)
4. ERROR (A serious issue where the software failed to perform a specific function)
5. FATAL (Highest - a severe error causing the entire application to abort)

If you initialize with `SimpLog("main.py", level="WARNING")`, only WARNING, ERROR, and FATAL messages will show up in your terminal. DEBUG and INFO will be silently ignored.

## Contributing
Found a bug or have an idea? Open an issue or PR. All feedback welcome!
