
i = input("Enter a number between 1 and 10: ")
number = int(i)
if number >= 10:
    print("The number you input is greater than 10, and therefore cannot be ran through this loop.")
else:
    while number <= 10:
        print(number)
        number = number + 1
    print("Done with Loop")
