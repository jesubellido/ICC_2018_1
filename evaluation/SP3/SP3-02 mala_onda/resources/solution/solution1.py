import sys
import os

def es_primo(x):
    if x==1:
        return False

    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def factores(x):
    lista = []
    for i in range(1,x+1):
        if x%i == 0:
            lista.append(i)
    return lista

def es_mala_onda(x):
    lst_factores = factores(x)
    for f in lst_factores:
        if es_primo(f) and f not in [2,3,5]:
            return False
    return True

#Programa
n = int(input())
if n>0:
    print(es_mala_onda(n))
else:
    print("Invalid input")
