import json
from models import ErrorLog
from dataclasses import asdict


frequency = {
    "ERROR":2,
    "INFO":1,
    "WARNING":1
}

# log is an Object
log = ErrorLog(
    level="ERROR",
    message="UART timeout",
    error_code=1001
)

def main():
    # serialize ( Write file )
    with open("frequency.json","w") as file:
        json.dump(frequency,file,indent=4 )

    # deserialize ( Read file )
    with open("config.json", "r") as file:
        config = json.load(file) # config is a dict: {"log_level": "ERROR", "output": "tool.log"}

        log_level = config.get("log_level")
        output = config.get("output")

        print(f"Log Level: {log_level}")
        print(f"Output File: {output}")

    # convert dataclass  OBJECT to DICTIONARY ( JSON cannot read OBJECT, only works with dict/list/string/int... )
    log_dict = asdict(log)

    with open("log_dict.json", "w") as file:
        json.dump(log_dict, file, indent=4)


if __name__ == "__main__":
    main()
