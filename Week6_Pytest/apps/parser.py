import re

from .models import LogEntry, ErrorLog, InfoLog, WarningLog

def parse_log(line):
    match = re.match(r"(\w+):\s(.+)", line)

    if not match:
        raise ValueError(f"Invalid log format: {line}")

    level = match.group(1)
    message = match.group(2)
    if level == "ERROR":
        log = ErrorLog(
            level=level,
            message=message,
            error_code=1001
        )
    if level == "INFO":
        log = InfoLog(
            level=level,
            message=message
        )
    if level == "WARNING":
        log = WarningLog(
            level=level,
            message=message
        )

    return log

def check_parser():
    with open("logs.txt", "r") as file:
        for line in file:
            try:
                log = parse_log(line)
                print(f"Parsed OK: {log.level} -> {log.message}")
            except ValueError as e:
                print(f"Parsed NOT OK: {e}")