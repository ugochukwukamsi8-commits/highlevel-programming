#!/usr/bin/python3
"""a module that handle standard opperators"""

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# Handle division by zero
if num2 != 0:
    print(f"Division: {num1} / {num2} = {num1 / num2}")
    print(f"Modulus: {num1} % {num2} = {num1 % num2}")
    print(f"Floor Division: {num1} // {num2} = {num1 // num2}")

    print("Division by zero is not allowed.")
    print("Modulus and Floor Division are not applicable due to division by zero.")
