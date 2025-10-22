from Util import *
# Punto_10_c1=[ 2/5, 3/5]
# mat_c1_10=[[3/5 ,2/5],[1/3 ,2/3]]
# Punto_10_c2=[ 3/4, 1/4]
# mat_c2_10=[[2/3 ,1/3],[1/10, 9/10]]
# print(entopia_posteriori(Punto_10_c2,mat_c2_10))

#PUNTO 12

# _,priori=Alfabeto_y_sus_probabilidades("abcacaabbcacaabcacaaabcaca")
# mat_prob_canal=mat_canal("abcacaabbcacaabcacaaabcaca","01010110011001000100010011")


# # _,priori=Alfabeto_y_sus_probabilidades("1101011001101010010101010100011111")
# # mat_prob_canal=mat_canal("1101011001101010010101010100011111","1001111111100011101101010111110110")

# # _,priori=Alfabeto_y_sus_probabilidades("110101100110101100110101100111110011")
# # mat_prob_canal=mat_canal("110101100110101100110101100111110011","110021102110022010220121122100112011")
# priori=[0.3,0.3,0.4]
# mat_prob_canal=[[0.4,0.4,0.2],
#          [0.3,0.2,0.5],
#          [0.3,0.4,0.3]]
# print(entropia_base_2(priori,saca_INFO_base_2(priori)))
# print(entopia_posteriori(priori,mat_prob_canal))

#PUNTO 13

canales = {
    "C1": {
        "probs_priori": [0.14, 0.52, 0.34],
        "matriz_canal": [
            [0.50, 0.30, 0.20],
            [0.00, 0.40, 0.60],
            [0.20, 0.80, 0.00]
        ]
    },
    "C2": {
        "probs_priori": [0.25, 0.25, 0.50],
        "matriz_canal": [
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.00, 0.50],
            [0.50, 0.00, 0.50, 0.00]
        ]
    },
    "C3": {
        "probs_priori": [0.12, 0.24, 0.14, 0.50],
        "matriz_canal": [
            [0.25, 0.15, 0.30, 0.30],
            [0.23, 0.27, 0.25, 0.25],
            [0.10, 0.40, 0.25, 0.25],
            [0.34, 0.26, 0.20, 0.20]
        ]
    }
}
canal="C3"
print(entropia_base_2(canales[canal]["probs_priori"],saca_INFO_base_2(canales[canal]["probs_priori"])))
print(entopia_posteriori(canales[canal]["probs_priori"],canales[canal]["matriz_canal"]))