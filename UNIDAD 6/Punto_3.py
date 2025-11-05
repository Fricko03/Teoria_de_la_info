

from Util_REAL import *

m1=[[0.7,0.0,0.3,0.0],
    [ 0.2,0.6,0.0,0.2]]

m2=[[0.9,0.0,0.1],
    [0.0,1.0,0.0],
    [0.1,0.1,0.8],
    [0.0,0.5,0.5]
    ]
pa=[0.5,0.5]
pb=Prob_de_b(pa,m1)
print(entropia_ruido(pa,m1))
print(info_mutua_a_b(pa,m1))
print(entropia_ruido(pb,m2))

print(info_mutua_a_b(pb,m2))
m3=mat_compuesta(m1,m2)
print(m3[0])
print(m3[1])
print(entropia_ruido(pa,m3))
print(info_mutua_a_b(pa,m3))
