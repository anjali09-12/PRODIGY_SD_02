import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")
    
    # Game loop
    while not guessed_correctly:
        # Prompt the user to input their guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Compare the guess with the generated number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

# Run the game
guessing_game()