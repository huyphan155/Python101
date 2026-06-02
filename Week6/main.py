from parser import parse_log
import json

def divide(a, b):
    if b == 0:
        raise ValueError("Invalid input, Divisor cannot be zero")
    print(a/b)

def check_parser():
    with open("logs.txt", "r") as file:
        for line in file:
            try:
                log = parse_log(line)
                print(f"Parsed OK: {log.level} -> {log.message}")
            except ValueError as e:
                print(f"Parsed NOT OK: {e}")

def load_config(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print("load_config() : Config file not found")
        raise # raise to main

    except json.JSONDecodeError as e:
        print("load_config() : Config file JSONDecodeError")
        raise # raise to main

def main():
    # divide(10, 2) #  True case
    # divide(10, 0) #  Invalid case
    # check_parser()
    # Json 1 : file not exist
    try:
        load_config("missing_config.json")
    except FileNotFoundError as e:
        print(f"MAIN : {e}")
    # Json 2 : Json file have incorrect format
    try:
        load_config("config_IncorrectFormat.json")
    except json.JSONDecodeError as e:
        print(f"MAIN : {e}")
    # Json 3 : normal file
    try:
        load_config("config.json")
        print("Successfully loaded config")
    except Exception as e:
        print(f"MAIN : {e}")


if __name__ == "__main__":
    main()
