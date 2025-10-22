from Util import *

# Obtener las probabilidades de los símbolos de salida de los canales propuestos en los
# ejercicios 1 y 3. Comparar los resultados obtenidos de dos maneras distintas: a partir de
# las secuencias de salida y utilizando las probabilidades a priori y la matriz del canal.


# _,priori=Alfabeto_y_sus_probabilidades("abcacaabbcacaabcacaaabcaca")
# _,prob_b_salida=Alfabeto_y_sus_probabilidades("01010110011001000100010011")
# mat_prob_canal=mat_canal("abcacaabbcacaabcacaaabcaca","01010110011001000100010011")
# prob_b=Prob_de_b(priori,mat_prob_canal)
# print(prob_b)
# print(prob_b_salida)
# _,priori=Alfabeto_y_sus_probabilidades("1101011001101010010101010100011111")
# _,prob_b_salida=Alfabeto_y_sus_probabilidades("1001111111100011101101010111110110")
# mat_prob_canal=mat_canal("1101011001101010010101010100011111","1001111111100011101101010111110110")
# prob_b=Prob_de_b(priori,mat_prob_canal)
# print(prob_b)
# print(prob_b_salida)
_,priori=Alfabeto_y_sus_probabilidades("110101100110101100110101100111110011")
_,prob_b_salida=Alfabeto_y_sus_probabilidades("110021102110022010220121122100112011")
mat_prob_canal=mat_canal("110101100110101100110101100111110011","110021102110022010220121122100112011")
prob_b=Prob_de_b(priori,mat_prob_canal)
print(prob_b)
print(prob_b_salida)
print(Prob_posteriori(priori,mat_prob_canal))
print(Prob_simultaneo(priori,mat_prob_canal))
