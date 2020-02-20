user_input = int(input("Enter a number to start: ")) #First number input by the user
user_raised = int(input("Enter a number to raise by: ")) #Second number input by the user

def raise_to_power (base_num, pow_num): #Function named raise_to_power that requires 2 parameters, base_num & pow_num. base_num is the first number, pow_num is the number the base_num is to be raised by. base_num ^pow_num
    result = 1 #One answer
    for index in range(pow_num): #For loop named index in the range of pow_num
        result = result * base_num #result = the result (1) * whatever the base_num is (user input)
    return result #returning the result

print(raise_to_power(user_input, user_raised)) #printing out the function with the inputs from the user which line up with the parameters