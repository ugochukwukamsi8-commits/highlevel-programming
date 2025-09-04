#!/usr/bin/python3
"""a module that implement the area of a triangle"""
def triangle(b,h):
    return 0.5*b*h


if __name__ == "__main__":
    b = int(input("enter the value of b"))
    h = int(input("enter the value of h"))
    print(triangle(b,h)) 