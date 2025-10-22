from Util import *
entrada_a="1101011001101010010101010100011111"
entrada_b="110101100110101100110101100111110011"
salida_a="1001111111100011101101010111110110"
salida_b="110021102110022010220121122100112011"

alf_a,probs_a=Alfabeto_y_sus_probabilidades(entrada_a)
mat_a=mat_canal(entrada_a,salida_a)

alf_b,probs_b=Alfabeto_y_sus_probabilidades(entrada_b)
mat_b=mat_canal(entrada_b,salida_b)
print(alf_a)
print(probs_a)
print(mat_a)
print(alf_b)
print(probs_b)
print(mat_b)
