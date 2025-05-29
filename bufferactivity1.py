def add_and_subtract(a, b):
    addition = a +b
    subtraction = a - b
    return addition,subtraction

#Example usage
num1 = float(input("Enter  the first number:"))
num2 = float(input("Enter the second number"))

sum_result, diff_result = add_and_subtract(num1,num2)

print(f"Addition: {sum_result}")
print(f"Subtraction: {diff_result}")