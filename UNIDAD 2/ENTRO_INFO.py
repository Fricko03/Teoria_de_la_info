import math 




def sacaprob(probs):
    return  [math.log2(1/s) for s in probs  ]

def entropia(lista_pro,lista_INFO):
   return  sum(s*p for s,p in zip(lista_pro,lista_INFO))

lista_pro=[0.1,0.3,0.4,0.2]
lista_INFO= sacaprob(lista_pro)
print("Probabilidades: ",[f"{p:.2f}"  for p in lista_INFO])

H= entropia(lista_pro,lista_INFO)
print(f"Entropia:{H:.2f}")