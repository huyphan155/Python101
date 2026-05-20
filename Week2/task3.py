import re
import argparse
import logging

def task1_simple_regex():
    log = "ERROR: UART timeout"

    match = re.match(r"(\w+):\s(.+)", log)
    # r = "raw string"". Make Python understand \ is string, not command code  (like \n)."
    # (\w+) capture "ERROR" in save into GROUP1 . () is for grouping
    # : Matches a colon (:)
    # \s,Match a (space, tab...)
    # (.+)  capture "UART timeout" in save into GROUP2
    print(match.group(1))
    print(match.group(2))

###################################################
# cmd and run : python task3.py logs.txt

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s", # format: Time - lever - message
    filename="tool.log",             # logging output file
    filemode="w"                     # "w" : overwrite, "a" continue
)

def task2_test_regex_parser_logging():
    # 1. Init parser
    parser = argparse.ArgumentParser(description="Something something")
    # 2. add argument
    parser.add_argument("input_path", help="path to a file")
    # 3. read user input
    args = parser.parse_args()

    # output : Frequency: {'ERROR': 2, 'INFO': 1, 'WARNING': 1}
    frequency = {}

    try:
        # open input file
        with open(args.input_path, "r") as file:
        # equal 2 line
        # file = open(args.input_path, "r")
        # file.close()

            for line in file:
                match = re.match(r"(\w+):\s(.+)", line)
                if match:
                    level = match.group(1)
                    message = match.group(2)
                    print(f"level:{level} , message: {message}")

                    # write data to frequency
                    if level not in frequency:
                        frequency[level] = 1
                    else:
                        frequency[level] += 1

                    # write if error into logging file "tool.log"
                    if level == "ERROR":
                        print("\tERROR detected and save to tool.log")
                        logging.error("ERROR detected")


        # show the Frequency data
        print("\nFrequency:",frequency)

    except Exception as e:
        print(e)

def main():
    print("task1_simple_regex\n")
    task1_simple_regex()
    print("\ntask2_test_regex_parser_logging\n")
    task2_test_regex_parser_logging()

if __name__ == "__main__":
    main()