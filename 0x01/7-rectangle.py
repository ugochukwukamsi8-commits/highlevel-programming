#!/usr/bin/python3
"""a module that implements the area of rectangle"""

def rectangle(l,w):
    return 0.5*l*w


if __name__ == "__main__":
    l = int(input("enter the value of l"))
    w = int(input("enter the value of w"))
    print(rectangle(l,w)) 