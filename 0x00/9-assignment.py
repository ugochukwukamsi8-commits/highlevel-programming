#!/usr/bin/python3
"""a module to create a standard assignment"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("\n--- Assignment Operations ---")

    # Simple Assignment (=)
x = num1
print(f"x = num1: x is now {x}")

    # Add and Assign (+=)
x += num2  # Equivalent to x = x + num2
print(f"x += num2: x is now {x}")

    # Subtract and Assign (-=)
x -= num1  # Equivalent to x = x - num1
print(f"x -= num1: x is now {x}")

    # Multiply and Assign (*=)
x *= num2  # Equivalent to x = x * num2
print(f"x *= num2: x is now {x}")

    # Divide and Assign (/=)
x /= num1  # Equivalent to x = x / num1
print(f"x /= num1: x is now {x}")

    # Modulus and Assign (%=)
x = num1 # Reset x for a clear modulus example
x %= num2 # Equivalent to x = x % num2
print(f"x %= num2: x is now {x}")

    # Floor Divide and Assign (//=)
x = num1 # Reset x for a clear floor division example
x //= num2 # Equivalent to x = x // num2
print(f"x //= num2: x is now {x}")

    # Exponentiate and Assign (**=)
x = num1 # Reset x for a clear exponentiation example
power = 2 # Define a small power for demonstration
x **= power # Equivalent to x = x ** power
print(f"x **= {power}: x is now {x}")