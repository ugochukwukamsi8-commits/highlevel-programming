#!/usr/bin/python3
"""a module to create a bitwise operation"""
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
print("Invalid input. Please enter integers only.")
print(f"\nOriginal numbers: num1 = {num1}, num2 = {num2}")
# Perform bitwise AND assignment
temp_num1_and = num1
temp_num1_and &= num2
print(f"num1 &= num2: {temp_num1_and}")
temp_num1_or = num1
temp_num1_or |= num2
print(f"num1 |= num2: {temp_num1_or}")
temp_num1_xor = num1
temp_num1_xor ^= num2
print(f"num1 ^= num2: {temp_num1_xor}")
shift_val = 1
temp_num1_lshift = num1
temp_num1_lshift <<= shift_val
print(f"num1 <<= {shift_val}: {temp_num1_lshift}")
temp_num1_rshift = num1
temp_num1_rshift >>= shift_val
print(f"num1 >>= {shift_val}: {temp_num1_rshift}")
