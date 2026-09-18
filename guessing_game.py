import random

def guessing_game():
    secret_number = random.randint(1,30)
    attempts = 5
    print("Welcome to the Guessing Game! Guess a number between 1 and 30. You have 5 attempts.")

    while attempts > 0:
        print(f"You have {attempts} attempt/s left.")
        guess = int(input("Enter your guess: " ))
        if guess == secret_number:
            print("Congratulations! You've guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
            attempts -= 1
        else:
            print("Too high! Try again.")
            attempts -= 1

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()