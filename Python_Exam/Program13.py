"""13. Palindrome Checker
- Write a program to check if a given string or number is a palindrome.
- Allow the user to input multiple values using a loop."""

def is_palindrome(value):
    reverse = ''
    for char in value:
        reverse = char + reverse
    if value == reverse :
        return True
    else:
        return False
while True:
    user_input = input("Enter a string or number (or type 'exit' to stop): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
