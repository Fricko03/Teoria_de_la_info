from Util import *

# ## x prob
# probs=[1/6]*6

# print(entropia_base_2(probs,saca_INFO_base_2(probs)))

# probs=[1/9,1/6,1/9,1/9,1/6,1/3]
# print(entropia_base_2(probs,saca_INFO_base_2(probs)))

# ## ej 4 

# alf=["x","y","z"]
# probs=[0.5,0.1,0.4]
# info=saca_INFO_base_2(probs)
# for i,c in enumerate(alf):
#     print(f"La informacion del simbolo {c} es {info[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f}",end="\n")

# print()  # Salto de línea entre bloques

# alf = ["0", "1"]
# probs = [0.5, 0.5]
# info = saca_INFO_base_2(probs)
# for i, c in enumerate(alf):
#     print(f"La informacion del simbolo {c} es {info[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f}")

# print()  # Salto de línea entre bloques

# alf = ["A","B","C","D"]
# probs = [0.1,0.3,0.4,0.2]
# info = saca_INFO_base_2(probs)
# for i, c in enumerate(alf):
#     print(f"La informacion del simbolo {c} es {info[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f}")

# ##EJERCICIO 5
# print()
# print()
# print()
# MENSAJE="ABDAACAABACADAABDAADABDAAABDCDCDCDC"

# alf,probs = Alfabeto_y_sus_probabilidades(MENSAJE)
# ordena = sorted(zip(alf, probs))
# alf, probs = map(list, zip(*ordena))
# for i, c in enumerate(alf):
#     print(f"La informacion del simbolo {c} es {probs[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f}")

# ## punto 6 
# print()
# print()
# print()

# alf=["a"]
# probs=[1/len(alf)]*len(alf)
# for i, c in enumerate(alf):
#     print(f"La informacion del simbolo {c} es {probs[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f}")


# ##ejercicio 7
# print()
# print()
# print()

# alf=["a","b","c","d"]
# probs=[1/len(alf)]*len(alf)
# for i, c in enumerate(alf):
#     print(f"La informacion del simbolo {c} es {probs[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f}")


# ##ejrcicio 9


# print(valor_W(0.25))
# print(valor_W(0.75))
# print(valor_W(0.5))
# print(valor_W(1))
# print(valor_W(0))

##ejercicio 11

#orden 2 


# alf=["x","y","z"]
# probs=[0.5,0.1,0.4]

# alfaextend,probextend=calc_exte(alf,probs,3)
# for i,c in enumerate(alfaextend):
#     print(f"La proabilidad  del simbolo {c} es {probextend[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f} y la entropia extemdidas es {entropia_base_2(probextend,saca_INFO_base_2(probextend)):.2f}",end="\n")

# print()  # Salto de línea entre bloques

# alf = ["0", "1"]
# probs = [0.5, 0.5]
# alfaextend,probextend=calc_exte(alf,probs,3)
# for i,c in enumerate(alfaextend):
#     print(f"La proabilidad  del simbolo {c} es {probextend[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f} y la entropia extemdidas es {entropia_base_2(probextend,saca_INFO_base_2(probextend)):.2f}",end="\n")

# print()  # Salto de línea entre bloques

# alf = ["A","B","C","D"]
# probs = [0.1,0.3,0.4,0.2]
# alfaextend,probextend=calc_exte(alf,probs,3)
# for i,c in enumerate(alfaextend):
#     print(f"La proabilidad  del simbolo {c} es {probextend[i]:.2f}")
# print(f"La entropia de la fuente es {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f} y la entropia extemdidas es {entropia_base_2(probextend,saca_INFO_base_2(probextend)):.2f}",end="\n")

# print()  # Salto de línea entre bloques


##ejercicio 13
# M=[[1/2,1/3,0],
#    [1/2,1/3,1],
#    [0,1/3,0]
# ]
# esta=Estacionario(M,0.001)
# print("Vector estacionario: ")
# for i in esta:
#     print(f"{i:.2f}",end="\t")
# print(f"La entropia de la fuente es {Entropia_con_mem(M,esta):.2f}",end="\n")



### punto 16
# mensaje="BBAAACCAAABCCCAACCCBBACCAABBAA"

# mat_t,alf=alfabeto_mat_con_mem(mensaje)

# if is_mem_nula(mat_t):
#     alf,probs=Alfabeto_y_sus_probabilidades(mensaje)
   
#     print(f"La fuente que origino ese mensaje es una fuente de memoria nula y tiene entropia= {entropia_base_2(probs,saca_INFO_base_2(probs)):.2f}")
# else:
#     esta=Estacionario(mat_t,0.0001)
#     print(f"La fuente que origino ese mensaje es una fuente de memoria no nula y tiene entropia= {Entropia_con_mem(mat_t,esta):.2f}")


##ejercicio 17
# M=[[1/2,0,0,1/2],
#    [1/2,0,0,0],
#    [0,1/2,0,0],
#    [0,1/2,1,1/2]
# ]
# M=[[1/3,0,1,1/2,0],
#    [1/3,0,0,0,0],
#    [0,1,0,0,0],
#    [1/3,0,0,0,1/2],
#    [0,0,0,1/2,1/2]
# ]
# esta=Estacionario(M,0.001)
# print("Vector estacionario: ")
# for i in esta:
#     print(f"{i:.2f}",end="\t")
# print()
# print(f"La entropia de la fuente es {Entropia_con_mem(M,esta):.2f}",end="\n")



























##########guia backup

##eje14

# alf=["a","b","c","d"]
# prob=[0.2,0.3,0.4,0.1]
# alfexte,probexte=extendida_bien(alf,prob,4)
# info=saca_INFO_base_2(probexte)
# entr=entropia_base_2(probexte,info)
# print(entr)


propiedades(["0","00","10"])