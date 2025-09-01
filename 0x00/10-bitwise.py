#!/usr/bin/python3
"""a module that handles bitwise operators"""

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))


# Bitwise AND 

result = num1 & num2
print(f"{num1} & {num2} = {result}")

# Bitwise OR  

result = num1 | num2
print(f"{num1} | {num2} = {result}")

# Bitwise XOR  

result = num1 ^ num2
print(f"{num1} ^ {num2} = {result}")

# Bitwise NOT  

result = ~num1 
print(f"~{num1} = {result}") 

# left shift 

result = num1 << 2
print(f"{num1} << 2 = {result}")

# Right shift 

result = num1 >> 2
print(f"{num1} >> 2 = {result}")