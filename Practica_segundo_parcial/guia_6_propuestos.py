from Util_REAL import *

# prob1=[1/3,1/3,1/3]

# c1=[[1, 0, 0,],[
#  0 ,0 ,1],
#  [0, 1, 0]]

# c2=[[ 1/2, 1/2, 0],
#  [0 ,1/4 ,3/4]]

# if (not is_not_ruidosa(c1)):
#     print(entropia_ruido(prob1,c1))
# else:
#     print("sin ruido")
    
# print(entropia_perdida(prob1,c1))
# prob2=[0.5,0.5]
# if (not is_not_ruidosa(c2)):
#     print(entropia_ruido(prob2,c2))
# else:
#     print("sin ruido")
    
# print(entropia_perdida(prob2,c2))


# punto 2
# prob1=[1/3,1/3,1/3]
# c1=[[1,0,0],[0,1,0],[0,0,1]]
# prob2=[1/3,1/3,1/3]
# c2=[[0.5,0.5,0],[0,1,0],[0,0,1]]
# prob3=[1/3,1/3,1/3]
# c3=[[0.5,0.5,0],[0,0,1],[0,0,1]]

# if (not is_not_ruidosa(c1)):
#     print(entropia_ruido(prob1,c1))
# else:
#     print("sin ruido")
    
# print(entropia_perdida(prob1,c1))
# print()
# if (not is_not_ruidosa(c2)):
#     print(entropia_ruido(prob2,c2))
# else:
#     print("sin ruido")
    
# print()
# print(entropia_perdida(prob2,c2))

# if (not is_not_ruidosa(c3)):
#     print(entropia_ruido(prob3,c3))
# else:
#     print("sin ruido")
    
# print(entropia_perdida(prob3,c3))

# prob 3

# prob=[1/3,1/3,1/3]
# # c1=[[1,0,0],[0,0.5,0.5],[0,4/6,2/6]]
# # c2=[[7/8,1/8,0],[1/10,8/10,1/10],[0,2/9,7/9]]
# # print(entropia_perdida(prob,c1))
# # print(entropia_perdida(prob,c2))

# #punto 4 .add()

# # P(Y|x1) = [P(y1|x1), P(y2|x1), P(y3|x1)]
# p_Y_given_x1 = [[1/4, 1/4, 2/4],[5/18, 10/18, 3/18], [0, 2/9, 7/9]]

# # Opción (a): P(X) = [P(x1), P(x2), P(x3)]
# p_X_a = [1/3, 1/3, 1/3]

# # Opción (b): P(X) = [P(x1), P(x2), P(x3)]
# p_X_b = [1/20, 5/20, 14/20]

# # Opción (c): P(X) = [P(x1), P(x2), P(x3)]
# p_X_c = [3/10, 4/10, 3/10]

# print(entropia_perdida(p_X_a,p_Y_given_x1))
# print(entropia_perdida(p_X_b,p_Y_given_x1))
# print(entropia_perdida(p_X_c,p_Y_given_x1))

#punto 5 
# prob=[1/3,1/3,1/3]
# # Matriz C1
# # Filas: x1, x2, x3
# # Columnas: y1, y2
# C1 = [
#     [1/2, 1/2],  # Fila x1
#     [0, 1],      # Fila x2
#     [1, 0]       # Fila x3
# ]
# # Matriz C2
# # Filas: x1, x2, x3
# # Columnas: y1, y2, y3
# C2 = [
#     [1/5, 1/5, 3/5],  # Fila x1
#     [1/6, 5/6, 0],    # Fila x2
#     [2/3, 0, 1/3]     # Fila x3
# ]
# # Matriz C3
# # Filas: x1, x2, x3
# # Columnas: y1, y2
# C3 = [
#     [2/8, 6/8],  # Fila x1
#     [1, 0],      # Fila x2
#     [0, 1]       # Fila x3
# ]
# print(entropia_ruido(prob,C1))
# print(entropia_perdida(prob,C1))
# print()
# print(entropia_ruido(prob,C2))
# print(entropia_perdida(prob,C2))
# print()
# print(entropia_ruido(prob,C3))
# print(entropia_perdida(prob,C3))


# # Matriz C1: P(S|A)
# #           s1     s2     s3     s4     s5
# C1 = [
#     [1/3, 1/2, 1/6, 0, 0],  # Fila a1
#     [0, 0, 0, 1, 0],      # Fila a2
#     [0, 0, 0, 0, 1]       # Fila a3
# ]

# # Vector de probabilidades de entrada P(A)
# p_A_C1 = [1/3, 1/3, 1/3]  # [p(a1), p(a2), p(a3)]


# # Matriz C2: P(S|A)
# #           s1     s2     s3
# C2 = [
#     [1, 0, 0],  # Fila a1
#     [1, 0, 0],  # Fila a2
#     [1, 0, 0],  # Fila a3
#     [0, 1, 0],  # Fila a4
#     [0, 0, 1]   # Fila a5
# ]

# # Vector de probabilidades de entrada P(A)
# p_A_C2 = [0.20, 0.15, 0.15, 0.30, 0.20]  # [p(a1), p(a2), p(a3), p(a4), p(a5)]


# # Matriz C3: P(S|A)
# #           s1     s2     s3
# C3 = [
#     [1, 0, 0],      # Fila a1
#     [1/2, 1/2, 0],  # Fila a2 (0.5, 0.5, 0)
#     [1, 0, 0],      # Fila a3
#     [0, 1, 0],      # Fila a4
#     [0, 0, 1]       # Fila a5
# ]

# # Vector de probabilidades de entrada P(A)
# p_A_C3 = [0.2, 0.1, 0.2, 0.3, 0.2]  # [p(a1), p(a2), p(a3), p(a4), p(a5)]


# print(is_not_ruidosa(C1))
# print(is_determinante(C1))
# print(entropia_ruido(p_A_C1,C1))
# print(entropia_perdida(p_A_C1,C1))
# print(info_mutua_formula(p_A_C1,C1 ))
# print()
# print(is_not_ruidosa(C2))
# print(is_determinante(C2))
# print(entropia_ruido(p_A_C2,C2))
# print(entropia_perdida(p_A_C2,C2))
# print(info_mutua_formula(p_A_C2,C2 ))
# print()
# print(is_not_ruidosa(C3))
# print(is_determinante(C3))
# print(entropia_ruido(p_A_C3,C3))
# print(entropia_perdida(p_A_C3,C3))
# print(info_mutua_formula(p_A_C3,C3 ))
# print()


# #punto 7
# mat=[[1,0,0],[0,0,1],[0,1,0]]
# print(is_determinante(mat))



#punto11 12 13
# mat=[[0.33,0.5,0.17,0,0],[0,0,0,1,0],[0,0,0,0,1]]
# # Matriz 1: P(B|A)
# # Filas: a1, a2, a3
# # Columnas: b1, b2, b3, b4, b5
# mat = [
#     [0.4, 0.2, 0.2, 0.1, 0.1],  # Fila a1
#     [0.4, 0.2, 0.3, 0.1, 0],    # Fila a2
#     [0, 0, 0, 0, 1]            # Fila a3
# # ]
# prob = [1/3, 1/3, 1/3]


# mat = [
#     [0.2, 0.3, 0.5],  # Fila a1
#     [0, 0, 1],        # Fila a2
#     [0, 0, 1]         # Fila a3
# ]

# genera_matriz_canal_reducido(mat,prob)

#PUNTO 14
# p1=[1]
# c1=[[1]]

# p2=[0.5,0.5]
# c2=[[1],[1]]
# c3=[[1,0],[0,1]]

# print(info_mutua_a_b(p1,c1))
# print(calcula_capacidad(c1))
# print()
# print(info_mutua_a_b(p2,c2))

# print(calcula_capacidad(c2))
# print()
# print(info_mutua_a_b(p2,c3))

# print(calcula_capacidad(c3))

#PUNTO 15 
# p1=[1]
# c1=[[0.5,0.5]]

# p2=[0.5,0.5]
# c2=[[0.5,0.5,0],[0,0,1]]
# c3=[[0.5,0.5,0,0],[0,0,0.5,0.5]]

# print(info_mutua_a_b(p1,c1))
# print(calcula_capacidad(c1))
# print()
# print(info_mutua_a_b(p2,c2))

# print(calcula_capacidad(c2))
# print()
# print(info_mutua_a_b(p2,c3))

# print(calcula_capacidad(c3))

#punto 16 n olo hago 


# PUNTO 17 18 

# prob=[0.5,0.5]

# mat =[[0.6,0.4],[0.2,0.8]]

# print(info_mutua_a_b(prob,mat))
# print(capacidad_binaria(mat,0.0001))


# mat=[[0.25,0.75],[0.9,0.1]]
# print(info_mutua_a_b(prob,mat))
# print(capacidad_binaria(mat,0.0001))

# # PUNTO 19 20
# prob=[]
# # mat=[[0.51,0.49],[0.72,0.28]]
# # capacidad,w=capacidad_binaria(mat,0.0001)
# # prob=[w,1-w]
# # print(info_mutua_a_b(prob,mat))
# # print(capacidad)
# # print(w)    
# mat=[[0.77,0.23],[0.2,0.8]]
# capacidad,w=capacidad_binaria(mat,0.00001)
# prob=[w,1-w]
# print(info_mutua_a_b(prob,mat))
# print(capacidad)
# print(w)


# SALTE AL PUNTO 22

# PUNTO 22
# prob=[0.5,0.5]
# mat=[[0.6,0.4],[0.2,0.8]]
# print(calcula_error(prob,mat))

# PUNTO 23 
# prob=[1/3,1/3,1/3]
# mat=[[0.6,0.3,0.1],[0.1,0.8,0.1],[0.3,0.3,0.4]]
# print(calcula_error(prob,mat))
# print()
# prob=[4/15,3/15,8/15]
# print(calcula_error(prob,mat))
# print()
# prob=[1/8,3/8,1/2]
# print(calcula_error(prob,mat))

# PUNTO 24 

prob=[5/8,1/8,2/8]
ma_1=[[0.6,0.3,0.1],[0.1,0.8,0.1],[0.3,0.3,0.4]]
ma_2=[[5/19,8/19,6/19],[0,1,0],[4/5,0,1/5]]
ma_3=[[1/2,0,1/2],[1/3,1/3,1/3],[0,1,0]]
print(calcula_error(prob,ma_1))
print()
print(calcula_error(prob,ma_2))
print()
print(calcula_error(prob,ma_3))

# PUNTO 25

