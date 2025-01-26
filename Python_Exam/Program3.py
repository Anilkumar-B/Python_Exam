"""3. Number Guessing Game
- Develop a program where the computer generates a random number between 1 and 100,
and the user guesses the number.
- Provide hints like &quot;Too High&quot; or &quot;Too Low.&quot;
- Use a loop to allow multiple attempts.
"""



import random

def number_guessing():
    number = random.randint(1, 100)  # Generate a random number
    guesses = 0  # Initialize guess counter

    while True:
        guess = input("Guess a number between 1 and 100: ")
        if guess.isdigit():
            guess = int(guess)
            guesses += 1  
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {guesses} attempts.")
                break  
        else:
            print("Invalid input. Please enter a whole number between 1 and 100.")

number_guessing()

    