from Util_REAL import *

probs=[0.1,0.09,0.12,0.09,0.1,0.12,0.12,0.14,0.12]

print(huffman_binario(probs))
print(shanon_binario(probs))
print(calculo_redundancia_rendimiento(probs,huffman_binario(probs)))
print(calculo_redundancia_rendimiento(probs,shanon_binario(probs)))
