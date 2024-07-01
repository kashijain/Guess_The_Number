import random
def guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")
    print('Type "quit" to exit the game.')
    while True:
        guess = input("Enter your guess: ")
        
        if (guess == "quit"):
            print("Thanks for playing! Goodbye.")
            break
        attempts += 1
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
if __name__ == "__main__":
    guess_game()
