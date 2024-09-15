import random

MIN_NUMBER = 1
MAX_NUMBER = 100
EASY_NUMBER = 10
MEDIUM_NUMBER = 5
HARD_NUMBER = 3

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print("You need to guess the number before you run out of chances.")
    print()

def select_difficulty():
    print("Please select the difficulty level:")
    print(f"1. Easy ({EASY_NUMBER} chances)")
    print(f"2. Medium ({MEDIUM_NUMBER} chances)")
    print(f"3. Hard ({HARD_NUMBER} chances)")
    choice = input("Enter your choice: ")

    if choice == '1':
        return EASY_NUMBER  # Easy: 10 chances
    elif choice == '2':
        return MEDIUM_NUMBER   # Medium: 5 chances
    elif choice == '3':
        return HARD_NUMBER   # Hard: 3 chances
    else:
        print("Invalid choice. Defaulting to Easy.")
        return EASY_NUMBER  # Default to Easy if invalid choice
def play_game():
    welcome_message()
    chances = select_difficulty()
    number_to_guess = random.randint(MIN_NUMBER,MAX_NUMBER)
    print(f"Great! Let's start the game. You have {chances} chances to guess the correct number.")    
    attempts = 0
    while chances > 0:
        guess = int(input("Enter your guess: "))
        attempts += 1
        chances -= 1

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Incorrect! The number is greater than your guess.")
        else:
            print("Incorrect! The number is less than your guess.")

        if attempts >= 2 and chances > 0:
            give_hint(number_to_guess)

        if chances > 0:
            print(f"You have {chances} chances left.")
        else:
            print(f"Game over! The correct number was {number_to_guess}.")

def play_again():
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == 'yes':
            return True
        elif response == 'no':
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def give_hint(number_to_guess):
    print("Here's a hint!")
    if number_to_guess % 2 == 0:
        print("- The number is even.")
    else:
        print("- The number is odd.")

    if number_to_guess % 3 == 0:
        print("- The number is divisible by 3.")
    
    if number_to_guess <= 50:
        print("- The number is in the range of 1 to 50.")
    else:
        print("- The number is in the range of 51 to 100.")

def run():
    while True:
        play_game()
        if not play_again():
            print("Thanks for playing! Goodbye.")
            break



if __name__ == '__main__':
    run()