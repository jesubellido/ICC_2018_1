import sys
import os

def es_primo(n):
    if n == 1:
        return False

    for i in range(1,n):
        if i != 1 and i != n and n%i == 0:
            return False

    return True

#Programa principal
m = int(input())
if m>0:
    for i in range(m):
        x = int(input())
        print(es_primo(x))
else:
    print("Invalid input")
