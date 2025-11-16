from Util_REAL import*
mat= [
        "00111000",
        "11000010","11011010","11011111","11100101","11100101"
    ]
c= [
    "01011011",
    "10000011",
    "10100100",
    "10000101",
    "10011110",
    "10011010"]
mensaje=bytearray()
matriz= mat
print(matriz)

for fila in c:
        
        byte_val = int(fila, 2)
        
        mensaje.append(byte_val)
        
# mensaje="amorr"
# imprimir_bytearray_en_binario(codificar_mensaje_paridad_impar(mensaje))

# # print(mensaje)
print(decodificar_corregir_paridad_impar(mensaje))