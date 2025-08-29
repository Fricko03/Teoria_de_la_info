
import random
import GUIA1_1

#FUENTE SIN MEMORIA SACAR ALFABETO PROB Y ENTROPIA

def a(mensaje):
    alfabeto=[]
    probabilidades=[]
    for c in mensaje:
        if (c not in alfabeto):
            alfabeto.append(c)
            probabilidades.append(1)
        else:
            probabilidades[alfabeto.index(c)] += 1
    return alfabeto,probabilidades
        
lista_alfabeto=[]
lista_prob=[]
mensaje="ABDAACAABACADAABDAADABDAAABDCDCDCDC"
lista_alfabeto,lista_prob= a(mensaje)
lista_prob=[x/len(mensaje) for x in lista_prob]

print(f"Alfabeto: {lista_alfabeto}")
print("Probabilidades: ",[f"{p:.2f}"  for p in lista_prob])
lista_inf=GUIA1_1.sacaprob(lista_prob)
print(f"Entropia:{GUIA1_1.entropia(lista_prob,lista_inf)}")

# def b(alfabeto,probabilidades):
#     frecuencia_acum=[]
#     frecuencia_acum.append(probabilidades[0])
#     for i in range(1,len(probabilidades)):
#         frecuencia_acum.append(probabilidades[i]+frecuencia_acum[i-1])
#     print(frecuencia_acum)
#     mensaje_generado=""
    
#     for i in range(len(mensaje)):
#         num = random.random()
#         cont=0
#         while num> frecuencia_acum[cont]:
#             cont+=1
#         mensaje_generado +=alfabeto[cont]
      
#     return mensaje_generado
# # lista_alfabeto2=["a","b","c","d"]
# # lista_prob2=[0.25,0.25,0.25,0.25]
# print(b(lista_alfabeto,lista_prob))