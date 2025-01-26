"""6. Prime Numbers in a Range
- Write a program that takes two numbers as input and prints all the prime numbers in
that range.
- Use a function to check if a number is prime."""


import math
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  
    if num % 2 == 0:  
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):  
        if num % i == 0:
            return False
    return True
def print_primes_in_range(start, end):
    if start > end:
        start, end = end, start

    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

while True:
    starting = int(input("Enter the start number: "))
    ending= int(input("Enter the end number: "))

    if starting < 1 or ending< 1:
        print("Both the start and end numbers should be greater than or equal to 1. Please try again.")
    else:
        print_primes_in_range(starting, ending)
        break
