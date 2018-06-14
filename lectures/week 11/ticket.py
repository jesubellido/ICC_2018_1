import sys
import os

t = '''
************************
*                      *
*      BOLETO          *
*                      *
************************
* FECHA: 10/12/2018    *
* NOMBRE:<NOMBRE>      *
* APELLIDO:<APELLIDO>  *
* PASAPORTE:<PASAPORTE>*
*                      *
************************
'''

name_t = "<NOMBRE>      "
apellido_t = "<APELLIDO>  "
pasaporte_t = "<PASAPORTE>"

name = input().ljust(len(name_t))
apellido = input().ljust(len(apellido_t))
pasaporte = input().ljust(len(pasaporte_t))

t = t.replace(name_t, name)
t = t.replace(apellido_t,apellido)
t = t.replace(pasaporte_t, pasaporte)

print(t)
