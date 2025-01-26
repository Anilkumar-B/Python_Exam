"""15. Leap Year Checker
- Write a program to check if a given year is a leap year.
- Allow the user to check multiple years.
"""

def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):   #logic : leap year is divisible by 4 and not by 100 or divisible by 400
        return True
    else:
        return False
    
while True:
    user_input = input("Enter a year to check if it's a leap year (or type 'exit' to stop): ")  #taking input from user
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    if user_input.isdigit():
        year = int(user_input)
        if leapYear(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print("Invalid input! Please enter a valid year.")
