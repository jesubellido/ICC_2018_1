import sys
import os

def mcd(a,b):
    max = 1
    for i in range(1,a+1):
        if a%i == 0 and b%i == 0:
           max = i
    return max

#Programa
a = int(input())
b = int(input())

if a>0 and b>0:
    print(mcd(a,b))
else:
    print("Invalid input")
