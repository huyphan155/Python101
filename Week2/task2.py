# pip install pyserial

from serial.tools import list_ports

ports = list_ports.comports()

for port in ports:
    print(port) # COM1 - Communications Port (COM1)
    print(port.device) # COM1
    print(port.description) # Communications Port (COM1)
    print(port.hwid) # abc\abc\0
    print(vars(port))




