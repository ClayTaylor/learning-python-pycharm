
i = input("Enter a number between 1 and 10: ") # Getting an input from the user
number = int(i) # Converting the input from the user to an integer
if number >= 10: # If Statement evaluating if the input from the user is Greater than or Equal to 10.
    print("The number you input is greater than 10, and therefore cannot be ran through this loop.")
else: # If the value is Less than or equal to 10, then run / print the values that are True using the Loop below.
    while number <= 10:
        print(number)
        number = number + 1
    print("Done with Loop")
