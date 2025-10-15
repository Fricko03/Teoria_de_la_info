from Util import *

mensaje="58784784525368669895745123656253698989656452121702300223659"
alf,probs=Alfabeto_y_sus_probabilidades(mensaje)

print(entropia_base_2(probs,saca_INFO_base_2(probs)))
print()
print(huffman_binario(probs))
print(shanon_binario(probs))
print()
print(longitud_media(huffman_binario(probs),probs))
print(calculo_redundancia_rendimiento(probs,huffman_binario(probs)))
print()
print(longitud_media(shanon_binario(probs),probs))
print(calculo_redundancia_rendimiento(probs,shanon_binario(probs)))