"""16. Odd and Even Separator
- Write a program that takes a list of numbers as input and separates them into odd and
even lists."""

even_numbers = []
odd_numbers = []


while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break 

    if user_input.isdigit():
        number = int(user_input)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    else:
        print("Invalid input! Please enter a valid number.")
        

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
