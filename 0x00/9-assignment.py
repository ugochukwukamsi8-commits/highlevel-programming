#!/usr/bin/python3
"""a module to create a standard assignment"""
# Get the first number from the user
num1_str = input("Enter the first number: ")
# Convert the input string to a float
num1 = float(num1_str)

# Get the second number from the user
num2_str = input("Enter the second number: ")
# Convert the input string to a float
num2 = float(num2_str)

print(f"\nOriginal values: num1 = {num1}, num2 = {num2}\n")

# Assignment operations
# = (Simple assignment)
x = num1
print(f"Simple assignment (x = num1): x = {x}")

# += (Add and assign)
x = num1  # Reset x for demonstration
x += num2
print(f"Add and assign (x += num2): x = {x}")

# -= (Subtract and assign)
x = num1  # Reset x for demonstration
x -= num2
print(f"Subtract and assign (x -= num2): x = {x}")

# *= (Multiply and assign)
x = num1  # Reset x
x *= num1
x /= num2
print(f"Divide and assign (x /= num2): x = {x}")
print(f"Modulus and assign (x %= num2): x = {x}")
print("Cannot perform modulus with zero.")
x //= num2
print(f"Floor divide and assign (x //= num2): x = {x}")
print("Cannot perform floor division by zero.")
