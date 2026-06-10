from dataclasses import dataclass


@dataclass
class LogEntry:
    level: str
    message: str

    def show(self):
        print(f"{self.level}: {self.message}")

@dataclass
class ErrorLog(LogEntry):
    error_code: int

    def show(self):
        print(
            f"[ERROR] {self.message}"
        )

@dataclass
class InfoLog(LogEntry):
    def show(self):
        print(
            f"[INFO] {self.message}"
        )

@dataclass
class WarningLog(LogEntry):
    def show(self):
        print(
            f"[WARNING] {self.message}"
        )