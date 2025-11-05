from matplotlib.mlab import detrend
from Util_REAL import *


# m=[[0.4,0.6,0.0,0.0,],
#    [0.0,0.0,0.5,0.5,],
#    [0.0,0.0,0.7,0.3]]

m=[[0.2 ,0.3, 0.5],
[0.0, 0.0, 1.0],
[0.0 ,0.0 ,1.0]]

# m=[[0.4, 0.0, 0.2, 0.4],
# [0.4, 0.3 ,0.2 ,0.1],
# [0.0, 0.3, 0.0 ,0.7]]
# # S
# m= [[0.0,0.0, 0.0, 0.5],
# [0.8,0.5, 0.2, 0.0],
# [0.0,0.0, 0.0, 0.5],
# [0.8,0.5, 0.2, 0.0]]

p1=[1/3,1/3,1/3]
p2=[1/4,1/4,1/4,1/4]
print(info_mutua_a_b(p1,m))
# print(entropia_base_2(p2,saca_INFO_base_2(p2)))
print("Ruido",entropia_ruido(p1,m))
print("Es determinante: ",is_determinante(m))
imprimir_matriz_normal(genera_matriz_canal_reducido(m))
# print(entropia_perdida(p2,m))
# print(entropia_salida(p2,m))
# print(entropia_priori(p2))



# imprimir_matriz_normal(m_reducida)
# print(entropia_ruido(p2,m_reducida))
# print(info_mutua_a_b(p2,m_reducida))
# print(is_determinante(m_reducida))
# m_reducida=reduce_mat(m,1,2)
# if (m_reducida!=None):
#     imprimir_matriz_normal(m_reducida)
#     print(entropia_ruido(p2,m_reducida))
#     print(info_mutua_a_b(p2,m_reducida))
#     print(is_determinante(m_reducida))
# else:
#     print("Mo es lineal")
# # reducir_iterativamente(m,p1)