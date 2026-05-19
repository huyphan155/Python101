#1.  read log file, filter WARNING / ERROR, Export new file

# Input : logs.txt
# Output new file : filtered_logs.txt
# ERROR: UART timeout
# WARNING: Low battery
# ERROR: CAN time out


from pathlib import Path

path = Path("logs.txt")

try:
    # open input file
    file = open(path, "r")
    # open output file
    file_new = open("filtered_logs.txt", "w")

    for line in file:
        if "ERROR" in line or "WARNING" in line:
            file_new.write(line)

    file.close()
    file_new.close()

    file_new = open("filtered_logs.txt", "r")
    # take data from new file
    data_new = file_new.read()

    print(data_new)

    # close files

    file_new.close()

except:
    print("Error")
