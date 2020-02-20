
try: # Defines to Python that we want to try the code.
    number = int(input("Enter a number ")) #Variable Number is equal to an input from the user and is converted/read as an integer.
    print(number) # Printing out the number the user entered.
except ZeroDivisionError: #Except is catching the ZeroDivisionError thrown if someone divides a number by zero.
    print("Can't divide by Zero") #Printing out a string on the console notifying the user they cannot divide by zero, instead of throwing the massive error Pytong returns and breaking the program.
except ValueError: #Except catching a ValueError if a user inputs anything but numbers into the input (i.e. letters), protecting the program from long error messages.
    print("Invalid Input") #Prints out a string on the conosole notifying the user they cannot enter anything but numbers into the input, else it will throw this error.
