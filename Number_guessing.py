import random

def play_game():
    secret_number = random.randint(1, 10)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10....")

    while True:
        guess = input("Enter your guess: ").strip()
        try:
            guess = int(guess)
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue
            if guess == secret_number:
                print("Congratulations! You guessed the number!")
                break
            else:
                print("Try again!")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    play_game()