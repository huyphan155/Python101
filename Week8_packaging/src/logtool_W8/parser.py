import re

from .models import ErrorLog, InfoLog, WarningLog

def parse_log(line):
    match = re.match(r"(\w+):\s(.+)", line)
    if match:
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