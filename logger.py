class Logger:
    def __init__(self):
        self.logs = []

    def log(self, msg):
        import time
        timestamp = time.strftime("%H:%M:%S")
        line = f"[{timestamp}] {msg}"
        self.logs.append(line)

        if len(self.logs) > 20:
            self.logs.pop(0)

    def get_logs(self):
        return "\n".join(self.logs)