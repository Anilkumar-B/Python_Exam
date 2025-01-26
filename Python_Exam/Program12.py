"""12. Pattern Generator
- Create a program that generates the following pattern based on user input `n`:
*
**
***
****
- Add an option to print the pattern in reverse."""

n = int(input("Enter the number of rows: "))

# Print the pattern in increasing order
for i in range(1, n + 1):
    print('*' * i)

# Ask if the user wants the reverse pattern
reverse_choice = input("Do you want to print the pattern in reverse? (yes/no): ").lower()

if reverse_choice == "yes":
    for i in range(n, 0, -1):
        print('*' * i)
