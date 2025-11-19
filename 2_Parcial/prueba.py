from Util_REAL_final import *

mensaje="TEORIA"

teoria_vec=[]
for i in mensaje:
    teoria_vec.append(bin(paridad_caracter(i))[2:].zfill(8))
print(teoria_vec)

imprimir_bytearray_en_binario(codificar_mensaje_con_paridad(mensaje))
mat=["00001001",
"10101001",
"10001011",
"10011111",
"10100101",
"10010011",
"10000010"]

print(decodificar_y_corregir_paridad(mat_a_byte(mat)))
# print(Hamming_errores_soluciones(teoria_vec))