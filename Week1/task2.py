# 1. Check log contain error,, simple CLI menu

log_data0 = "ERROR: UART timeout"
log_data1 = "INFO: Boot success"

def check_error(log):
    if "ERROR" in log:
        print("Found ERROR")
    else:
        print("No ERROR")

check_error(log_data0)
check_error(log_data1)

# 2. Count number of appear
logs = [
    "ERROR",
    "INFO",
    "ERROR",
    "WARNING",
    "ERROR"
]

def count_error(logs):
    count = 0
    for log in logs:
        if "ERROR" in log:
            print("Found ERROR")
            count += 1
    if count == 0:
        print("No ERROR")
    else:
        print(f"ERROR count {count}")

count_error(logs)

#3. Simple CLI menu
def CLI_menu():
    while True:
        print("- 1. Celsius -> Fahrenheit")
        print("- 2. Fahrenheit -> Celsius")
        print("- 0. Exit")
        option = input()
        if option == "1":
            celsius = int(input("enter temperature in Celsius : "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(f'Fahrenheit = {(fahrenheit)}')
        elif option == "2":
            fahrenheit = int(input("enter temperature in Fahrenheit : "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f'Celsius = {(celsius)}')
        elif option == "0":
            break
        else:
            print("Invalid option")

CLI_menu()