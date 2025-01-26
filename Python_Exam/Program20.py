"""20. FizzBuzz Problem
- Write a program that prints numbers from 1 to 100, but:
- Prints &quot;Fizz&quot; for multiples of 3.
- Prints &quot;Buzz&quot; for multiples of 5.
- Prints &quot;FizzBuzz&quot; for multiples of both 3 and 5."""

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)