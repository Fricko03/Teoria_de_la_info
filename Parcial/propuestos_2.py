from Util import *
# ## 1
# alf=["a","b","c","d"]
# prob=[1/2,1/4,1/16,3/16]

# print(entropia_base_2(prob,saca_INFO_base_2(prob)))


# # ##3
print()
print()
print()
mensaje="ABDAACAABACADAABDAADABDAAABDCDCDCDC"
alf,prob=Alfabeto_y_sus_probabilidades(mensaje)
ordena = sorted(zip(alf, prob))
alfa, prob = map(list, zip(*ordena))
print(alf)
print(prob)
info=saca_INFO_base_2(prob)
entr=entropia_base_2(prob,info)
print(info)
print(entr)

# # ##4
# # probs=[1/9,1/6,1/9,1/9,1/6,1/3]
# # print(entropia_base_2(probs,saca_INFO_base_2(probs)))

# # ##13

# # with open(r"C:\Users\tomas\Teoria_de_la_info\Parcial\a.raw", "r") as f:
# #     next(f)
# #     next(f)
# #     contenido = f.read()  # lee todo el archivo como un solo string


# # pixeles = [x for x in contenido.split()]
# # alf,prob=Alfabeto_y_sus_probabilidades(pixeles)
# # ordena = sorted(zip(alf, prob))
# # alf, prob = map(list, zip(*ordena))

# # print(alf)
# # print(prob)

# #16
# # S

# ## 31

# # M=[[0.1,0.2,0.2],
# #    [0.3,0.2,0.4],
# #    [0.6,0.6,0.4]
# # ]
# # esta=Estacionario(M,0.001)
# # print("Vector estacionario: ")
# # for i in esta:
# #     print(f"{i:.2f}",end="\t")
# # print(f"La entropia de la fuente es {Entropia_con_mem(M,esta):.2f}",end="\n")



# # Verifica si el siguiente código es unívocamente decodificable y/o instantáneo:
# S = ["A", "B", "C", "D"]
# Código = [0, 10, 110, 111]
# propiedades(S)



# # Comprueba si las longitudes {1, 2, 3, 3} de un alfabeto binario cumplen la inecuación de Kraft. ¿Se puede construir un código instantáneo con esas longitudes?
# print(calcula_kraf_en_base_tam([1,2,3,3],2))
# # Una fuente con alfabeto {a, b, c, d} tiene probabilidades {0.5, 0.25, 0.125, 0.125}.

# # Calcula su entropía.
# probs=[0.5, 0.25, 0.125, 0.125]
# print("entropia",entropia_base_2(probs,saca_INFO_base_2(probs)))

# # Propón un código binario que intente ser compacto y compara su longitud media con la entropía.
# cod=["0","10","110","111"]
# print(is_compacto(cod,probs))
# print(longitud_media(cod,probs))

# # Modela el movimiento de un coche como fuente de Markov con las siguientes reglas:
# M=[
#     [0.3,0.5,0.2],
#     [0.2,0.3,0.5]
    
# ]


# # Repite la dirección anterior con prob. 0.5.

# # Gira a la derecha con prob. 0.3.

# # Gira a la izquierda con prob. 0.2.
# # a) Representa la fuente con un diagrama de estados.
# # b) Escribe la matriz de transición.
# # c) Explica cómo obtendrías la distribución estacionaria y la entropía del sistema.


####reehecho

probs=[0.1,0.3,0.4,0.2]

print(saca_INFO_base_2(probs))
print(entropia_base_2(probs,saca_INFO_base_2(probs)))




##13
print("-------------13----------------")
alfabet=["f1","f2","f3","f4"]
probs=[0.1,0.3,0.4,0.2]

alfa_ex,prob_ext=calc_exte(alfabet,probs,3
                           )
print(entropia_base_2(prob_ext,saca_INFO_base_2(prob_ext)))


##23

M=[
    [120/150,192/2400,0,99/1100],
    [27/150,1920/2400,33/1350,33/1100],
    [0,168/2400,1200/1350,88/1100],
    [3/150,120/2400,117/1350,880/1100]
    
    
]

print(Estacionario(M,0.0000001))

