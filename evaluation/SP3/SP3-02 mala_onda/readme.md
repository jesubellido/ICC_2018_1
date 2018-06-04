## Mala Onda

### Description

Calcula si un número es mala onda.

### Problem Statement
Los números *Mala Onda* son aquellos números cuyos factores primos (divisores que además son primos) son 2,3 ó 5.  Por ejemplo:

- **6** es un número *mala onda* por que tiene los factores 1,2,3 y 6; de los cuales solo 2 y 3 son factores primos.
- **7** no es un número mala onda porque tiene los factores 1 y 7 de los cuales 7 es el único factor primo y éste no pertenece al conjunto de factores primos necesarios para ser un número mala onda.

Crea un programa que dado un número entero positivo $n$ (ingresado por el usuario), calcule si es un número *mala onda* o no

- **factores** recibe como parámetro un número entero positivo y retorna una lista de todos los divisores.
- **es_primo** que recibe como parámetro un número entero positivo y retorna True si el número es primo o False en caso contrario.
- **es_mala_onda** recibe como parámetro un número positivo y retorna True si el número es mala onda on False en caso contrario.


### Input Format
- - La primera línea corresponde al número entero positivo $n$.

### Constraints
- $ 0 \lt n $

### Output Format
- Si las entradas son correctas, True o False para indicar que el número ingresado en un número *mala onda*.
- Si las entradas no son correctas, imprimir "Invalid input".

### Test Cases
- TestCase 00 [input](resources/tests/input/input00.txt) [output](resources/tests/output/output00.txt)
- TestCase 01 [input](resources/tests/input/input01.txt) [output](resources/tests/output/output01.txt)
- TestCase 02 [input](resources/tests/input/input02.txt) [output](resources/tests/output/output02.txt)
- TestCase 03 [input](resources/tests/input/input03.txt) [output](resources/tests/output/output03.txt)
- TestCase 04 [input](resources/tests/input/input04.txt) [output](resources/tests/output/output04.txt)
- TestCase 05 [input](resources/tests/input/input05.txt) [output](resources/tests/output/output05.txt)
- TestCase 06 [input](resources/tests/input/input06.txt) [output](resources/tests/output/output06.txt)
- TestCase 07 [input](resources/tests/input/input07.txt) [output](resources/tests/output/output07.txt)
- TestCase 08 [input](resources/tests/input/input08.txt) [output](resources/tests/output/output08.txt)
- TestCase 09 [input](resources/tests/input/input09.txt) [output](resources/tests/output/output09.txt)
- TestCase 10 [input](resources/tests/input/input10.txt) [output](resources/tests/output/output10.txt)
- TestCase 11 [input](resources/tests/input/input11.txt) [output](resources/tests/output/output11.txt)
- TestCase 12 [input](resources/tests/input/input12.txt) [output](resources/tests/output/output12.txt)
### Tags
- function, list

### Solutions
- [Solution 1](resources/solution/solution1.py)
