#!/usr/bin/env python3

""" 
Spirals of square with increasing length
"""

import turtle as tt

tt.speed(0);

def square(length):
    for i in range(4):
        tt.forward(length)
        tt.right(90)

for i in range(1000):
        square(i)
        tt.right(5)
