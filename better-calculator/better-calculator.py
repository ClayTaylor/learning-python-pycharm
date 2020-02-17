
num1 = float(input("Enter the First Number: "))
op1 = input("Enter the First Operator: ")
num2 = float(input("Enter the Second Number: "))
#num3 = float(input("Enter the Third Number: "))

if op1 == "+":
    print(num1 + num2)
elif op1 == "-":
    print(num1 - num2)
elif op1 == "/":
    print(num1 / num2)
elif op1 == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")