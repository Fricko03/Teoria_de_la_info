from Util import *

columna_codigo_1 = [
    "0100100", 
    "0101000", 
    "0010010", 
    "0100000"
]

columna_codigo_2 = [
    "0100100", 
    "0010010", 
    "0101000", 
    "0100001"
]

columna_codigo_3 = [
    "0110000", 
    "0000011", 
    "0101101", 
    "0100110"
]

print(Hamming_errores_soluciones(columna_codigo_1))
print(Hamming_errores_soluciones(columna_codigo_2))
print(Hamming_errores_soluciones(columna_codigo_3))
a,_,m=Hamming_errores_soluciones(columna_codigo_1)
print(a,_,m)
