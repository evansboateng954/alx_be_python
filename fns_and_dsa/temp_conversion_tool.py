FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FARENHEIT_TO_CELCIUS_FACTOR
    return temperature *  FARENHEIT_TO_CELCIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return temperature * CELSIUS_TO_FAHRENHEIT_FACTOR
temperature = float(input("Enter temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if unit == "C":
    print(convert_to_fahrenheit(temperature))

elif unit =="F":
    print(convert_to_celsius(temperature))

else:
    print("Invalid unit")
