import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()  # You don't need to convert input to str() as input() returns a string by default

    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20")

    count_guesses = 0
    while True:
        count_guesses += 1
        print("Take a guess:")
        try:
            guess = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number {number} in {count_guesses} guesses!")
            break

# Call the function to start the game
guess_the_number()
