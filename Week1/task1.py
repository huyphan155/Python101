# 1
def number_input():
    num = float(input("enter number to calculate average : "))
    return num

num1 = number_input()
num2 = number_input()
num3 = number_input()

print(f'average = {((num1+num2+num3)/3)}')

#2
def convert_temperature():
    print("- Convert Celsius to Fahrenheit , press C. \n- Convert Fahrenheit to Celsius , press F.")
    option = input().upper() # use .upper() so 'f' or 'F' is oke
    if option == "C":
        celsius = int(input("enter temperature in Celsius : "))
        fahrenheit = (celsius * 9/5) + 32
        print(f'Fahrenheit = {(fahrenheit)}')
    elif  option == "F":
        fahrenheit = int(input("enter temperature in Fahrenheit : "))
        celsius = (fahrenheit - 32) * 5/9
        print(f'Celsius = {(celsius)}')
    else:
        print("Invalid option")


convert_temperature()
#3
log_data = "ERROR: UART timeout"

result = log_data.split(":")

print(result[0])
print(result[1].strip())
# result: ['ERROR', ' UART timeout']
