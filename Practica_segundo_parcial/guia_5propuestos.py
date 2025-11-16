from Util_REAL import *

# alf,prob=Alfabeto_y_sus_probabilidades("abcacaabbcacaabcacaaabcaca")
# # print(alf)
# # print(prob)
# print(mat_canal("abcacaabbcacaabcacaaabcaca","01010110011001000100010011"))

#punto 2
X_1= "1101011001101010010101010100011111"
Y_1= "1001111111100011101101010111110110"
print()
x_2= "110101100110101100110101100111110011"
y_2= "110021102110022010220121122100112011"

# imprimir_matriz_normal(mat_canal(Y_1,X_1))
# print()
# imprimir_matriz_normal(mat_canal(y_2,x_2))

# print(Alfabeto_y_sus_probabilidades(Y_1))
# print(Alfabeto_y_sus_probabilidades(y_2))
#punto 3
# alf,prob=Alfabeto_y_sus_probabilidades(Y_1)

# print(Prob_de_b(prob,mat_canal(Y_1,X_1)))
# print(Alfabeto_y_sus_probabilidades(x_2))

#punto 4 5 

# mat_ej1=mat_canal("abcacaabbcacaabcacaaabcaca","01010110011001000100010011")
# alf_1,prob_ej1= Alfabeto_y_sus_probabilidades("abcacaabbcacaabcacaaabcaca")
# # print(Alfabeto_y_sus_probabilidades(y_2))
# mat_c1=mat_canal(Y_1,X_1)

# mat_c2=mat_canal(y_2,x_2)
# alf_c1,prob_c1=(Alfabeto_y_sus_probabilidades(Y_1))
# alf_c2,prob_c2=(Alfabeto_y_sus_probabilidades(y_2))
# imprimir_matriz_normal((Prob_posteriori(prob_ej1,mat_ej1)))
# print()
# imprimir_matriz_normal(Prob_posteriori(prob_c1,mat_c1))
# print()
# imprimir_matriz_normal(Prob_posteriori(prob_c2,mat_c2))

# imprimir_matriz_normal(Prob_simultaneo(prob_ej1,mat_ej1))
# print()
# imprimir_matriz_normal(Prob_simultaneo(prob_c1,mat_c1 ))
# print()
# imprimir_matriz_normal(Prob_simultaneo(prob_c2,mat_c2))
#   
# punto7

# alf=["a","b","c"    ]
# prob=[0.3,0.3,0.4]
# mat=[[0.4,0.4,0.2],[0.3,0.2,0.5],[0.3,0.4,0.3]
       
# ]
# print(Prob_de_b(prob,mat))
# print()
# imprimir_matriz_normal(Prob_posteriori(prob,mat))
# print()
# imprimir_matriz_normal(Prob_simultaneo(prob,mat))

#punto 8
# prob=[0.5,0.5]
# mat=[[1,0],[0,1]]

# print(Prob_de_b(prob,mat))
# print()
# imprimir_matriz_normal(Prob_posteriori(prob,mat))
# print()
# imprimir_matriz_normal(Prob_simultaneo(prob,mat))


# punto 9 
# prob=[0.2,0.8]
# mat=[[1,0],[0,1]]

# print(Prob_de_b(prob,mat))
# print()
# imprimir_matriz_normal(Prob_posteriori(prob,mat))
# print()
# imprimir_matriz_normal(Prob_simultaneo(prob,mat))



#punto 10 

# alf_7=["a","b","c"    ]
# prob_7=[0.3,0.3,0.4]
# mat_7=[[0.4,0.4,0.2],[0.3,0.2,0.5],[0.3,0.4,0.3]
       
# ]
# mat_ej1=mat_canal("abcacaabbcacaabcacaaabcaca","01010110011001000100010011")
# alf_1,prob_ej1= Alfabeto_y_sus_probabilidades("abcacaabbcacaabcacaaabcaca")
# # print(Alfabeto_y_sus_probabilidades(y_2))
# mat_c1=mat_canal(Y_1,X_1)

# mat_c2=mat_canal(y_2,x_2)
# alf_c1,prob_c1=(Alfabeto_y_sus_probabilidades(Y_1))
# alf_c2,prob_c2=(Alfabeto_y_sus_probabilidades(y_2))

# print(entopia_posteriori(prob_ej1,mat_ej1))
# print()
# print(entopia_posteriori(prob_c1,mat_c1))
# print()
# print(entopia_posteriori(prob_c2,mat_c2))
# print()   
# print(entopia_posteriori(prob_7,mat_7))

#punto 11_a
# pron=[2/5,3/5]
# # mat=[[3/5,2/5],[2/6,4/6]]
# pron=[3/5,1/4]
# mat=[[2/3,1/3],[1/10,9/10]]
# print(entropia_priori(pron))
# print(entopia_posteriori(pron,mat))

#punto 13
# pron=[0.25,0.25,0.50]
# mat=[[0.25,0.25,0.25,0.25],[0.25,0.25,0.,0.5],[0.5,0.,0.5,0.]]
# print(Prob_de_b(pron,mat))
# imprimir_matriz_normal(Prob_posteriori(pron,mat))
# print()
# imprimir_matriz_normal(Prob_simultaneo(pron,mat))
# print()
# print(entropia_priori(pron))
# print(entopia_posteriori(pron,mat))

#punto 13 c2 156 de la vieja

# Matriz P(B|A) - Probabilidades condicionales
# Filas: a1, a2, a3, a4
# Columnas: b1, b2, b3, b4
# pron=[0.12,0.24,0.14,0.5]
# mat = [
#     [0.25, 0.15, 0.30, 0.30],  # Fila a1
#     [0.23, 0.27, 0.25, 0.25],  # Fila a2
#     [0.10, 0.40, 0.25, 0.25],  # Fila a3
#     [0.34, 0.26, 0.20, 0.20]   # Fila a4
# ]


# print(Prob_de_b(pron,mat))
# imprimir_matriz_normal(Prob_posteriori(pron,mat))
# print()
# imprimir_matriz_normal(Prob_simultaneo(pron,mat))
# print()
# print(entropia_priori(pron))
# print(entopia_posteriori(pron,mat))



#punto 14 15
# prob=[0.5,0.5]
# mat=[[0.5,0.5],[0,1]]
# prob=[0.25,0.25,0.25,0.25]
# mat=[[0.5,0.5,0,0],[0,1,0,0],[0,1/3,1/3,1/3],[0,0,0,1]]
# # prob=[0.25,0.25,0.25,0.25]
# # mat=[[0.5,0.5,0],[0,0,1],[0,1,0],[0,0,1]]
# 
# prob=[0.5,0.5]#0.25,0.25,0.25,0.25]
# mat=[[0.3,0.3,0.4],[0.3,0.3,0.4]]#0.5,0.5,0],[0,0,1],[0,1,0],[0,0,1]]
# prob=[0.25,0.25,0.30,0.20]
# mat=[[0.25,0.5,0.25],[0.25,0.30,0.45],[0.3,0.3,0.4],[0.5,0,0.5]]
# print(entropia_ruido(prob,mat))
# print(info_mutua_a_b(prob,mat))
# print(info_mutua_b_a(prob,mat     ))
# print(info_mutua_formula(prob,mat))


#punto 20

# mat_ej1=mat_canal("abcacaabbcacaabcacaaabcaca","01010110011001000100010011")
# alf_1,prob_ej1= Alfabeto_y_sus_probabilidades("abcacaabbcacaabcacaaabcaca")
# # print(Alfabeto_y_sus_probabilidades(y_2))
# mat_c1=mat_canal(Y_1,X_1)

# mat_c2=mat_canal(y_2,x_2)
# alf_c1,prob_c1=(Alfabeto_y_sus_probabilidades(Y_1))
# alf_c2,prob_c2=(Alfabeto_y_sus_probabilidades(y_2))
# pron=[0.25,0.25,0.50]
# mat=[[0.25,0.25,0.25,0.25],[0.25,0.25,0.,0.5],[0.5,0.,0.5,0.]]
# print(entropia_afin(prob_ej1,mat_ej1))
# print(entropia_afin(prob_c1,mat_c1  ))
# print(entropia_afin(prob_c2,mat_c2))
# print(entropia_afin(pron,mat))

# punto 21

# Alfabetos
alfabeto_A_canal1 = ['a1', 'a2']
alfabeto_B_canal1 = ['b1', 'b2']

# Probabilidades a priori P(A)
prob_A_canal1 = [0.5, 0.5]

# Matriz de probabilidades condicionales P(B|A)
matriz_canal1 = [
    [1, 0],  # Fila A1
    [0, 1]   # Fila A2
]
# Alfabetos
alfabeto_A_canal2 = ['a1', 'a2']
alfabeto_B_canal2 = ['b1', 'b2']

# Probabilidades a priori P(A)
prob_A_canal2 = [0.5, 0.5]

# Matriz de probabilidades condicionales P(B|A)
matriz_canal2 = [
    [0.9, 0.1],  # Fila A1
    [0.3, 0.7]   # Fila A2
]
# Alfabetos
alfabeto_A_canal3 = ['a1', 'a2', 'a3']
alfabeto_B_canal3 = ['b1', 'b2', 'b3', 'b4']

# Probabilidades a priori P(A)
prob_A_canal3 = [0.25, 0.25, 0.50]

# Matriz de probabilidades condicionales P(B|A)
matriz_canal3 = [
    [0.25, 0.25, 0.25, 0.25],  # Fila A1
    [0.25, 0.25, 0,    0.5],   # Fila A2
    [0.50, 0,    0.5,  0]    # Fila A3
]
print(propiedad_simetrica(prob_A_canal1,matriz_canal1))
print(info_mutua_a_b(prob_A_canal1,matriz_canal1))
print(info_mutua_b_a(prob_A_canal1,matriz_canal1))
print()
print(propiedad_simetrica(prob_A_canal2,matriz_canal2))
print(info_mutua_a_b(prob_A_canal2,matriz_canal2))
print(info_mutua_b_a(prob_A_canal2,matriz_canal2))
print()
print(propiedad_simetrica(prob_A_canal3,matriz_canal3))
print(info_mutua_a_b(prob_A_canal3,matriz_canal3))
print(info_mutua_b_a(prob_A_canal3,matriz_canal3))
print()