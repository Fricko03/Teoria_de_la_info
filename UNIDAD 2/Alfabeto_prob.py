
import random
import ENTRO_INFO

#FUENTE SIN MEMORIA SACAR ALFABETO PROB Y ENTROPIA

def Alfabeto_y_sus_probabilidades(mensaje):
    alfabeto=[]
    probabilidades=[]
    for c in mensaje:
        if (c not in alfabeto):
            alfabeto.append(c)
            probabilidades.append(1)
        else:
            probabilidades[alfabeto.index(c)] += 1
    return alfabeto,probabilidades
        


def Generador_mensaje(alfabeto,probabilidades):
    frecuencia_acum=[]
    frecuencia_acum.append(probabilidades[0])
    for i in range(1,len(probabilidades)):
        frecuencia_acum.append(probabilidades[i]+frecuencia_acum[i-1])
    print(frecuencia_acum)
    mensaje_generado=""
    
    for i in range(len(mensaje)):
        num = random.random()
        cont=0
        while num> frecuencia_acum[cont]:
            cont+=1
        mensaje_generado +=alfabeto[cont]
      
    return mensaje_generado

# prueba
# lista_alfabeto=[]
# lista_prob=[]
# mensaje="ABDAACAABACADAABDAADABDAAABDCDCDCDC"
# lista_alfabeto,lista_prob= Alfabeto_y_sus_probabilidades(mensaje)
# lista_prob=[x/len(mensaje) for x in lista_prob]

# print(f"Alfabeto: {lista_alfabeto}")
# print("Probabilidades: ",[f"{p:.2f}"  for p in lista_prob])
# lista_inf=ENTRO_INFO.sacaprob(lista_prob)
# print(f"Entropia:{ENTRO_INFO.entropia(lista_prob,lista_inf)}")
# # lista_alfabeto2=["a","b","c","d"]
# # lista_prob2=[0.25,0.25,0.25,0.25]
# print(Generador_mensaje(lista_alfabeto,lista_prob))