import sys
import os

def factores(x):
    lista = []
    for i in range(1,x+1):
        if x%i == 0:
            lista.append(i)
    return lista


n = int(input())
if n>0:
    lst_factores = factores(n)
    for f in lst_factores:
        print(f)
else:
    print("Invalid input")
