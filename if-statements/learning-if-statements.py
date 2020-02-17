
is_male = True
is_tall = True


if is_male and is_tall:
    print("You are a tall male.")

elif is_male and not(is_tall):
    print("You are a male, but you are not tall.")
elif not(is_male) and is_tall:
    print("You are not a male, but you are tall.")
else:
    print("You are neither male nor tall.")

# if Statements can be used when I want my code to execute code when certain conditions are True and other conditions if they are False.
# 1) Boolean - A named variable that defines if something is True or False
# 2) if - First step, and if is not True, will move on to the next section of code. If True, will execute the code inside of it.
# 3) else - condition ran if the 'if' statement is not true.
# 4) or - used to enhance & add complexity to if statements. One or the other needs to be true and the code will run.
# 5) and - both conditions have to be True for the code to execute.
# 6) elif - "Else If"
# 7) not - Negates a True or False condition. i.e. True becomes False and False becomes True.

