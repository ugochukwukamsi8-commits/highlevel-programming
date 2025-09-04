#!/usr/bin/python3
"""a module that handles fizzbuzz operations"""

num = int(input("Enter your number:")) 
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5==0:
    print("Buzz")
elif sum % 3 == 0:
    print("Fizz")
else:
    print("invalid")