from Util_REAL import *
M1 = [
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0]
]


M2 = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.8],
    [0.0, 0.0, 1.0, 0.0],
    
]

M3 = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3]
]

M4 = [
    [0.0, 0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]
print(is_uniforme(M3))
print(calcula_capacidad(M1))
print(calcula_capacidad(M2))
print(calcula_capacidad(M3))
print(calcula_capacidad(M4))

