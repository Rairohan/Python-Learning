# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 20:15:40 2023

@author: Rohan Rai
"""

"""sum of first 5 natural number"""
x = int(input("enter the number"))
sum = 0
while ( x > 0):
    sum += x
    x -= 1
print("the sum is ", sum)