# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:51:39 2023

@author: Rohan Rai
"""

""" Largest and smallest among three numbers"""
x = int(input("enter the number:"))
y = int(input("enter the number:"))
z = int(input("enter the number:"))
if(x > y) and (x > z):
    largest = x
elif(y >x) and (y > z):
     largest = y
else: 
    largest = z
print("the largest among three is :",largest)
if(x < y) and (x < z):
    smallest = x
elif(y < x) and(y < z):
    smallest = y
else:
    smallest = z
print("the smallest number is :", smallest)
