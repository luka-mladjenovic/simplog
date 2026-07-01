import datetime

class SimpLog:

    def __init__(self, name, level="INFO", file_path=None):

        self.name = name.upper()

        # Map textual levels to numbers
        self.levels = {
            "DEBUG": 1,
            "INFO": 2,
            "WARNING": 3,
            "ERROR": 4,
            "FATAL": 5
        }

        self.min_level = level.upper()
        self.file_path = file_path

    def log(self, level_name, message):

        # Safely get the level to prevent crashes on typos
        current_val = self.levels.get(level_name, 2)
        min_val = self.levels.get(self.min_level, 2)

        # Only print if the message level meets or exceeds the minimum threshold
        if current_val >= min_val:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_string = f"[{timestamp}] [{self.name}] [{level_name}] {message}"

            print(log_string)

            # Only write to file if a file path was provided
            if self.file_path:
                with open(self.file_path, "a", encoding="utf-8") as f:
                    f.write(log_string + "\n")

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
