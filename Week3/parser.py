import re
from models import LogEntry, ErrorLog, InfoLog, WarningLog

def parse_log(line):
    match = re.match(r"(\w+):\s(.+)", line)
    if match:
        log = LogEntry(
            level=match.group(1),
            message=match.group(2)
        )
    return log