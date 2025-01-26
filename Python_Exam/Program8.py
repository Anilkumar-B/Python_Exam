"""8. Multiplication Table Generator
- Create a program to generate a multiplication table for any number provided by the user.
- Allow the user to specify the range of the table.
"""

Get_Input = int(input("Enter any number to get multiplication table: "))

if Get_Input == 0:
    print("Multiplication table for 0 will be all zeros.")
else:
    
    # while loop for allowing user to enter valid range
    while True:
        range_input = int(input("Enter the range: "))
        if range_input <= 0:
            print("Please enter a positive range.")
        else:
            break

    # for loop for table generation
    for i in range(1, range_input + 1):
        print(f"{Get_Input} X {i} = {Get_Input * i}")
