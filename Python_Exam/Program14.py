"""14. Factorial Calculator
- Create a program to calculate the factorial of a number using a loop.
- Include error handling for negative numbers."""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

user_input = input("Enter a number : ")

if user_input.isdigit():
    number = int(user_input)
    if number >= 0:
        print(f"The factorial of {number} is: {factorial(number)}")
    else:
        print("Please enter a non-negative number.")
else:
    print("Invalid input! Please enter a valid non-negative number.")
