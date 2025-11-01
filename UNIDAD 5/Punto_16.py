from Util import *

P_C11 = [0.70, 0.30]

M_C11 = [
    [0.7, 0.3],
    [0.4, 0.6]
]


P_C2 = [0.50, 0.50]

M_C2 = [
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
]


P_C3 = [0.25, 0.50, 0.25]

M_C3 = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.5, 0.5, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]


P_C4 = [0.25, 0.25, 0.25, 0.25]

M_C4 = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]


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
P_C1=canales[canal]["probs_priori"]
M_C1=canales[canal]["matriz_canal"]

print("Entropia a priori ",entropia_base_2(P_C1,saca_INFO_base_2(P_C1)))
print("Entropia a salida",entropia_salida(P_C1,M_C1))
print("Entropia ruido",entropia_ruido(P_C1,M_C1))
print("Entropia perdida",entropia_perdida(P_C1,M_C1))
print("Entropia afin",entropia_afin(P_C1,M_C1))
print("Info",info_mutua_a_b(P_C1,M_C1))
      
      
