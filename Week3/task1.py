""""
from dataclasses import dataclass
@dataclass
class LogEntry:
    level: str
    message: str

EQUAL :

class LogEntry:
    def __init__(self, level, message):
        self.level = level
        self.message = message

"""
import re
from pathlib import Path
from dataclasses import dataclass

@dataclass
class LogEntry:
    level: str
    message: str

    def show(self):
        print(f"{self.level}: {self.message}")

def parse_log(line):
    match = re.match(r"(\w+):\s(.+)", line)
    if match:
        log = LogEntry(
            level=match.group(1),
            message=match.group(2)
        )
    return log

# TASK 1 :
input_log = "ERROR: UART timeout"
"""
OUT PUT : 
LogEntry(
    level="ERROR",
    message="UART timeout"
)
"""

log = parse_log(input_log)
print(log)

# TASK 2 :
input_path = Path("logs.txt")
"""
OUT PUT:

    logs = [
        LogEntry("ERROR","UART timeout"),
        LogEntry("INFO","Boot success"),
        LogEntry("ERROR","CAN timeout")
    ]
    
    {
       "ERROR":2,
       "INFO":1
    }
"""

logs = []
frequency = {}

with open(input_path, "r") as file:
    for line in file:
        log = parse_log(line)
        logs.append(log)
        if log:
            level = log.level
            if level not in frequency:
                frequency[level] = 1
            else:
                frequency[level] += 1

print(logs)
# show the Frequency data
print("\nFrequency:", frequency)

#D2_Task1
@dataclass
class ErrorLog(LogEntry):
    error_code: int

    def show(self):
        print(
            f"[ERROR] {self.message}"
        )

@dataclass
class InfoLog(LogEntry):
    pass

    def show(self):
        print(
            f"[INFO] {self.message}"
        )

@dataclass
class WarningLog(LogEntry):
    pass

    def show(self):
        print(
            f"[WARNING] {self.message}"
        )


class LogManager:
    def __init__(self):
        self.logs = []

    def add_log(self, log):
        self.logs.append(log)

    def get_logs(self):
        return self.logs

manager = LogManager()


logError = ErrorLog(
    level="ERROR",
    message="UART timeout",
    error_code=1001
)
manager.add_log(logError)

logInfo = InfoLog(
    level="INFO",
    message="Boot success",
)
manager.add_log(logInfo)

logWarning = WarningLog(
    level="WARNING",
    message="Low battery",
)
manager.add_log(logWarning)

print(logError)
print(logInfo)
print(logWarning)

frequencyD2 = {}

for line in manager.get_logs():
    line.show()
    level = line.level
    if level not in frequencyD2:
        frequencyD2[level] = 1
    else:
        frequencyD2[level] += 1

# show the frequencyD2 data
print("\nfrequencyD2:", frequencyD2)
