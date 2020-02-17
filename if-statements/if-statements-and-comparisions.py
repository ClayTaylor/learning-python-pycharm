
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(0, 1, 2))

# Introduction to Comparison Values
# 1) >= -Greater than or Equal to
# 2) <= -Less than or Equal to
# 3) == -Equal in value
# 4) != -Not equal in value
# 5) > -Greater than
# 6_ < -Less than