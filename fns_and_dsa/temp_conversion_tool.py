FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature *  FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return temperature * CELSIUS_TO_FAHRENHEIT_FACTOR

temperature = float(input("Enter temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")

elif unit =="F":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")

else:
    print("Invalid unit")
