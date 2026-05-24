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







