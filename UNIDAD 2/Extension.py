def calc_exte(alfeto,probabilidades,n):
    if (n==1):
        return alfabeto,probablilidades
    else:
        alfabeto_extendido,probablilidades_extendido=calc_exte(alfeto,probablilidades,n-1)
        alfabeto_extendido=alfabeto_extendido*len(alfabeto)
        
        probablilidades_extendido=probablilidades_extendido*len(probabilidades)
        
        alfabeto_aux=[letra for letra in alfeto for i in range(len(alfabeto)**(n-1))]#len(alfabeto_extendido)//len(alfabeto)) ]
        print(alfabeto_aux)
        alfabeto_extendido=[alfabeto_aux[x]+alfabeto_extendido[x] for x in range (len(alfabeto_extendido)) ]
        
        prob_aux=[prob for prob in probabilidades for i in range(len(probablilidades_extendido)//len(probabilidades)) ]
       
        probablilidades_extendido=[prob_aux[x]*probablilidades_extendido[x] for x in range (len(probablilidades_extendido)) ]
        
    return alfabeto_extendido,probablilidades_extendido

def extendida_bien(alfabeto, probabilidades,n):
    if(n==1):
        return alfabeto,probabilidades
    else:
      alfabeto_extendido,probablilidades_extendido=extendida_bien(alfabeto,probablilidades,n-1)
      alfabeto_extendido=alfabeto_extendido*len(alfabeto)
      probablilidades_extendido=probablilidades_extendido*len(probabilidades)  
      fin=0
      for i,letra in enumerate(alfabeto):
        #   fin=len(alfabeto)**(n-1)*i
        #   print(fin,"fin")
          for j in range(fin,len(alfabeto)**(n-1)):
                print(j,"soy j, soy fin",fin)
                alfabeto_extendido[j]=letra+alfabeto_extendido[j]
                probablilidades_extendido[j]=probabilidades[i]*probablilidades_extendido[j]
          fin+=len(alfabeto)**(n-1)
         
              
    return alfabeto_extendido,probablilidades_extendido
              
alfabeto=["a","b","c"]
probablilidades=[0.4,0.3,0.3]
print("Ingrese su extensión")
n=int(input())



#alfabeto_extendido,probablilidades_extendido=calc_exte(alfabeto,probablilidades,n)
alfabeto_extendido,probablilidades_extendido=extendida_bien(alfabeto,probablilidades,n)

for letras, prob in zip(alfabeto_extendido, probablilidades_extendido):
    print(letras, f"{prob:.2f}")