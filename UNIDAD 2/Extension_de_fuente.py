import ENTRO_INFO 
def calc_exte(alfabeto,probabilidades,n):
    if (n==1):
        return alfabeto,probabilidades
    else:
        alfabeto_extendido,probablilidades_extendido=calc_exte(alfabeto,probabilidades,n-1)
        alfabeto_extendido=alfabeto_extendido*len(alfabeto)
        
        probablilidades_extendido=probablilidades_extendido*len(probabilidades)
        
        alfabeto_aux=[letra for letra in alfabeto for i in range(len(alfabeto)**(n-1))]#len(alfabeto_extendido)//len(alfabeto)) ]
        print(alfabeto_aux)
        alfabeto_extendido=[alfabeto_aux[x]+alfabeto_extendido[x] for x in range (len(alfabeto_extendido)) ]
        
        prob_aux=[prob for prob in probabilidades for i in range(len(probablilidades_extendido)//len(probabilidades)) ]
       
        probablilidades_extendido=[prob_aux[x]*probablilidades_extendido[x] for x in range (len(probablilidades_extendido)) ]
        
    return alfabeto_extendido,probablilidades_extendido

def extendida_bien(alfabeto, probabilidades,n):
    if(n==1):
        return alfabeto,probabilidades
    else:
      alfabeto_extendido,probablilidades_extendido=extendida_bien(alfabeto,probabilidades,n-1)
      alfabeto_extendido=alfabeto_extendido*len(alfabeto)
      probablilidades_extendido=probablilidades_extendido*len(probabilidades)  
      fin=0
      for i,letra in enumerate(alfabeto):
          for j in range(fin,fin+len(alfabeto)**(n-1)):
                print(j,"soy j, soy fin",fin)
                alfabeto_extendido[j]=letra+alfabeto_extendido[j]
                probablilidades_extendido[j]=probabilidades[i]*probablilidades_extendido[j]
          fin+=len(alfabeto)**(n-1)
         
              
    return alfabeto_extendido,probablilidades_extendido

#prueba
              
# alfabeto=["A","B","C","D"]#"1","2","3","4","5","6"]
# probablilidades=[0.1,0.3,0.4,0.2]

# print("Ingrese su extensión")
# n=2#int(input())



# #alfabeto_extendido,probablilidades_extendido=calc_exte(alfabeto,probablilidades,n)
# alfabeto_extendido,probablilidades_extendido=calc_exte(alfabeto,probablilidades,n)

# for letras, prob in zip(alfabeto_extendido, probablilidades_extendido):
#     print(letras, f"{prob:.3f}")
    
# print(f"Suma de probabilidades extendidas a {n} es {sum(probablilidades_extendido)} ")

# print(
#     f"Entropia de la fuente extendida es {ENTRO_INFO.entropia(probablilidades_extendido,ENTRO_INFO.sacaprob(probablilidades_extendido)):.2f}\n"
#     f"Entropia de la fuente compun {ENTRO_INFO.entropia(probablilidades,ENTRO_INFO.sacaprob(probablilidades)):.2f}, "
#     f"{n*ENTRO_INFO.entropia(probablilidades,ENTRO_INFO.sacaprob(probablilidades))} "
# )
def ghol(probi):
     
    print(probi) 
    
probis="puto"
ghol(probis)