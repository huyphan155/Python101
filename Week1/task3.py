# 1.  parse log to dictionary
from idlelib.outwin import OutputWindow

log_data = "ERROR: UART timeout"

# Output
# {
#     "level": "ERROR",
#     "message": "UART timeout"
# }

data_handle = log_data.split(":")
# data_handle[0] = "ERROR"
# data_handle[1] = " UART timeout"
# or level, message = log_data.split(":")

dict_data = {
    "level": data_handle[0],
    "message": data_handle[1].strip(),
}

print(dict_data)

#########################################################################
#2. message frequency
#list
logs = [
    "ERROR",
    "INFO",
    "ERROR",
    "WARNING",
    "ERROR",
    "INFO"
]

# Output
# {
#     "ERROR": 3,
#     "INFO": 2,
#     "WARNING": 1
# }

frequency = {}

for log in logs:
    if log not in frequency:
        frequency[log] = 1
    else:
        frequency[log] += 1

print(frequency)

#########################################################################
#3 frame parser
frame = "ID=0x123 DATA=01 02 03"
# Output
# {
#     "id": "0x123",
#     "data": "01 02 03"
# }


parts = frame.split(" DATA=")
# parts[0] = ID=0x123
# parts[1] = 01 02 03

frame_handle = {
    "id": parts[0].split("=")[1],
    "data": parts[1]
}

print(frame_handle)

#########################################################################
#4 message handle
logs = [
    "ERROR: UART timeout",
    "INFO: Boot success",
    "ERROR: CAN timeout",
    "WARNING: Low battery",
    "ERROR: UART timeout"
]

# Output
# {
#    "ERROR": 3,
#    "INFO": 1,
#    "WARNING": 1
# }

frequency4 = {}

for log in logs:
    level, detail = log.split(":")
    # level = ERROR, detail = UART timeout
    if level not in frequency4:
        frequency4[level] = 1
    else:
        frequency4[level] += 1

print(frequency4)





