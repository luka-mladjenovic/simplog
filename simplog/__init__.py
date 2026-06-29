import datetime

class SimpLog:

    def __init__(self, level="INFO"):

        # Map textual levels to numbers
        self.levels = {
            "DEBUG": 1,
            "INFO": 2,
            "WARNING": 3,
            "ERROR": 4,
            "FATAL": 5
        }

        self.min_level = level.upper()

    def log(self, level_name, message):

        # Safely get the level to prevent crashes on typos
        current_val = self.levels.get(level_name, 2)
        min_val = self.levels.get(self.min_level, 2)

        # Only print if the message level meets or exceeds the minimum threshold
        if current_val >= min_val:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{level_name}] {message}")

    # --- Shortcut Methods --- 

    def debug(self, message):
        self.log("DEBUG", message)
        
    def info(self, message):
        self.log("INFO", message)
        
    def warn(self, message):
        self.log("WARNING", message)
        
    def error(self, message):
        self.log("ERROR", message)
        
    def fatal(self, message):
        self.log("FATAL", message)
