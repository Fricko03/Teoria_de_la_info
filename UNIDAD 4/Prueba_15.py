from Util import *
ALFABETO_LISTA = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O', 'R', 'S'] 
# Codificación ajustada a la longitud del alfabeto (ejemplo de 4 bits para simplicidad)
CODIFICACION_LISTA = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010"]

MENSAJE_ORIGINAL = "DEBES CODIFICAR"

print(f"Alfabeto Fuente (Lista): {ALFABETO_LISTA}")
print(f"Mensaje Original: '{MENSAJE_ORIGINAL}'")

# --- CODIFICACIÓN ---
mensaje_codificado_bytes = codificacion_binaria(ALFABETO_LISTA, CODIFICACION_LISTA, MENSAJE_ORIGINAL)
print("\n--- Resultado de Codificación ---")
print(imprimir_bytearray_en_binario(mensaje_codificado_bytes))

# --- DECODIFICACIÓN ---
mensaje_decodificado = decodificacion_binaria(ALFABETO_LISTA, CODIFICACION_LISTA, mensaje_codificado_bytes)
print("\n--- Resultado de Decodificación ---")
print(f"Mensaje Decodificado: '{mensaje_decodificado}'")

# Verificación
assert MENSAJE_ORIGINAL == mensaje_decodificado
print(f"\nVerificación exitosa: {MENSAJE_ORIGINAL == mensaje_decodificado} ✅")