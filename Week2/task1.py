#1.  read log file, filter WARNING / ERROR, Export new file

# Input : logs.txt
# Output new file : filtered_logs.txt
# ERROR: UART timeout
# WARNING: Low battery
# ERROR: CAN time out
# {'ERROR': 2, 'WARNING': 1}

from pathlib import Path

input_path = Path("logs.txt")
new_path = Path("filtered_logs.txt")

counter = {
    "ERROR":0,
    "WARNING":0
}

try:
    # open input file
    file = open(input_path, "r")
    # open output file
    file_new = open(new_path, "w")

    for line in file:
        if "ERROR" in line:
            counter["ERROR"] += 1
            print(line.strip())
            file_new.write(line)

        if "WARNING" in line:
            print(line.strip())
            file_new.write(line)
            counter["WARNING"] += 1

    print(counter)

    file.close()
    file_new.close()

except Exception as e:
    print(e)
