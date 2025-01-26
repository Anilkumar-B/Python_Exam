"""2. Temperature Conversion Tool
- Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin
based on user input.
- Use functions for each conversion."""


# Function to convert Celsius to Fahrenheit and Kelvin
def CelsiusConversion(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin


# Function to convert Fahrenheit to Celsius and Kelvin
def FahrenheitCoversion(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return celsius, kelvin


# Function to convert Kelvin to Celsius and Fahrenheit
def KelvinConversion(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, fahrenheit

def temperature_conversion():
    User_Input = input('''Which temperature scale are you going to enter?  
    (You have three options: Celsius, Fahrenheit, and Kelvin)
    So, please enter the Units (Either C or F or K): ''').upper()  
    Temperature_input = float(input("Enter the temperature value: "))
    
    if User_Input == 'C':
        fahrenheit, kelvin = CelsiusConversion(Temperature_input)
        print(f"Entered temperature is {Temperature_input}°C")
        print(f"{Temperature_input}°C = {round(fahrenheit,3)}°F")
        print(f"{Temperature_input}°C = {round(kelvin,3)}K")
    
    elif User_Input == 'F':
        celsius, kelvin = FahrenheitCoversion(Temperature_input)
        print(f"Entered temperature is {Temperature_input}°F")
        print(f"{Temperature_input}°F = {round(celsius,3)}°C")
        print(f"{Temperature_input}°F = {round(kelvin,3)}K")
    
    elif User_Input == 'K':
        celsius, fahrenheit = KelvinConversion(Temperature_input)
        print(f"Entered temperature is {Temperature_input}K")
        print(f"{Temperature_input}K = {round(celsius,3)}°C")
        print(f"{Temperature_input}K = {round(fahrenheit,3)}°F")
    
    else:
        print("Invalid input! Please enter C, F, or K for the temperature scale.")


temperature_conversion()
