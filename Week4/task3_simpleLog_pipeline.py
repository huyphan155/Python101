from api_client import upload_log
from dataclasses import asdict
from parser import parse_log
from manager import LogManager
import json

def task3_simpleLog_pipeline():
    print('\nTask3')
    """
        logs.txt
            ↓
        parse_log()
            ↓
        LogManager
            ↓
        count_frequency()
            ↓
        result.json
            ↓
        upload frequency
            ↓
        upload all logs
    """
    manager = LogManager()
    with open("logs.txt", "r") as file:
        for line in file:
            log = parse_log(line)
            manager.add_log(log)

    frequency = manager.count_frequency()
    # show the frequency data
    print("\nfrequencyD2:", frequency)

    # log the frequency data into "result.json"
    with open("result.json", "w") as file:
        json.dump(
            frequency,
            file,
            indent=4
        )

    # UPDATE frequency
    response = upload_log(frequency)
    print(f'Status_code of frequency upload: {response.status_code}')

    # update log
    for log in manager.get_logs():
        log_dict = asdict(log)

        response = upload_log(log_dict)
        print(f'Status_code of log upload: {response.status_code}')