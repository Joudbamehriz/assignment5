# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:00:12 2024

@author: joahb

this code finds the zeros of a tanh(x)=0.5x in the interval 1-4 with a tolerance of 1*10^-5
using both the bisection method and newton raphson 
"""
import math 
import numpy as np 

def function(x):
    return math.tanh(x)-0.5*(x)

def derfunction(x):
    return 0.5-math.tanh(x)**2 

def NRF(guess):
    print("running code for Newton method...")
    p = guess
    i = 0
    while np.absolute(function(p))>10e-5:
        fp=function(p)
        derfp=derfunction(p) 

        p_new= p-(fp/derfp)
        p = p_new
        i = i + 1
    print("the solution of tanh(x)=0.5x in the interval 1-4 is",p)
    print("the number of iterations needed is", i)
print("running code for Newton method...")
guess=float(input('give a guess in the interval 1-4: '))
NRF(guess)
print ('\n')
def bisection(a,b):
    print("running code for bisection method...")
    i = 0
    while function(a)-function(b)>10e-5 and i < 1000:
        if function(a)*function(b) < 0: 
            c=(a+b)/2
            if function(c)*function(a)<0:
                b = c 
            elif function(c)*function(b)<0:
                a=c
        else:
            b = b + 1 
            a = a - 1
        i = i+ 1
        if i == 999:
            print("the bisection method fails in this range, try different values for a and b.")
    if i < 1000:
        #print("f(a) after is {} and f(b) after is {}.".format(function(a), function(b)))
        solution = (a+b)/2
       # print("a after is {} and b after is {}.".format(a,b))
        print ("solution is {}".format(solution))
        print("the number of iterations is {}".format(i))
bisection(1,4)

