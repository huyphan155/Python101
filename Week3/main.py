"""
main.py
   |
   +--> parser.py
   |        |
   |        +--> models.py
   |
   +--> manager.py
   |
   +--> models.py
"""

from parser import parse_log
from manager import LogManager
from models import ErrorLog, InfoLog, WarningLog


def main():
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


if __name__ == "__main__":
    main()
