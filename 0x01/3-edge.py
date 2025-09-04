#!/usr/bin/python3
"""a module that handles if and logical operations"""
age =int(input("Enter your age"))

if age <=10 and age <=17:
    print("You are a teenager")
elif age >=18 and age <=40:
    print("You are an adult")
else:
    print("You are old")       