# -*- coding: utf-8 -*-
"""

@author: PC
"""
import math
from functools import reduce

def add(first, second):
    return (first+second)


def subtract(first, second):
    return (first-second)

def multiply(first, second):
    return (first*second)

def divide(first, second):
    #if second == 0:
     #   return ('Division Not Allowed')
    return (first/second)

#root, where first = number, second is the root 
def root(first, second):
    return(first**(1/second))     

#power, where first is the number and second is the power
def power(first, second):
    return (first**second)

#factorial
def factorial(first):
    return(math.factorial(first))

# square of a number    
def square(first):
    return (first**2)

#cube of a number
def cube(first):
    return (first**3)

#Trigonometric functions
def sin(first):
    return (math.sin(first))

def cos(first):
    return (math.cos(first))

def tan(first):
    return (math.tan(first))


seq = [1,2,3,4,5]
#type(seq)
    # Lambda and Reduce functions for mathematical functions on a list
def add_Func(seq):    #Addition
    return (reduce(lambda x, y: x+y, seq))
    
    #Subtraction
def sub_Func(seq):
    return reduce(lambda x, y: x-y, seq)
    
    #Multiplication
def mult_Func(seq):    
    return reduce(lambda x, y: x*y, seq)
    
    #Division
def div_Func(seq):
    return reduce(lambda x, y: x/y, seq)
    
    
    # Map and Lambda functions for list elements
    # Squared function on a list of elements
def sqr_Func(seq):    
    return [x**2 for x in seq]
sqr_Func(seq)    
    #Square Root function on a list of elements
def sqr_Rt(seq):
    sqr_rt = list(map(lambda x: x**0.5,seq))
    return sqr_rt
sqr_Rt(seq)


# Calculate Pi using Generator Technique
#def pi():
#  numerator = 2.0
#  denominator = 1.0
#  while True:
#    yield numerator/denominator
#    if numerator < denominator:
#      numerator += 2
#    else:
#      denominator += 2
#
#p = pi()
#
#res = 1.0
#for i in range(10000000):
#  res *= next(p)
#
#print (res*2)