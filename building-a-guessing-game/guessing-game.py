
secret_word = "milkshake" #Creating a Secret Word
guess = "" # Created a guess variable which is the input variable in the while loop.
guess_count = 0 # Variable counting the amount of guesses the user has input.
guess_limit = 5 # Variable counting the limit the user can input.
out_of_guesses = False # Variable detecting if the user has run out of guesses.

while guess != secret_word and not(out_of_guesses): # While Loop checking to see if the input is NOT equal to the secret word AND if the user has not run out of guesses.
    if guess_count < guess_limit: # If Statement checking to see if the guess count remains lower than the guess limit.
        guess = input("Enter your best guess: ") # input from the user
        guess_count += 1 # Incrementing the guess count by one of the above remains true.
        print("Guess Count: " + str(guess_count) + "/5")
    else:
        out_of_guesses = True # Once the user has reached their guess limit, then the out_of_guesses variable becomes true.

if out_of_guesses: # If True, then the following prints on the console and the user loses the game.
    print("You have run out of guesses, and failed the game.")
else: # If false, then the user has guessed the correct secret word and has won the game.
    print("You win!")
