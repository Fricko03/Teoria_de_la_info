import random
import copy
import Fuente_memoria_no_nula
import ENTRO_INFO
def a(mensaje):
    
    alfabeto=[]
   
    for c in mensaje:
        if (c not in alfabeto):
            alfabeto.append(c)

    n=len(alfabeto)  
    alfabeto.sort()
    mat_trans = [[0]*n for _ in range(n)]    
    for i in range(n):
        for j in range(n):
            sum=0
            for k in range(len(mensaje)-1):
                if (mensaje[k:k+2]==(alfabeto[i]+alfabeto[j])):
                    sum+=1
            mat_trans[j][i]=sum
    
       
    normalizar(mat_trans)        
    return mat_trans,alfabeto

def normalizar(matriz):
  
    filas = len(matriz)
    columnas = len(matriz[0])

# recorremos columnas
    for j in range(columnas):
        suma = sum(matriz[i][j] for i in range(filas))  # suma de la columna j
        if suma != 0:
            for i in range(filas):
                if (sum!=0):
                    matriz[i][j] /= suma
    
def b(alfabeto,mat_fun,long_mensaje):
    n=len(alfabeto)  
    frecuencia_acum_mat = copy.deepcopy(mat_fun) 

    
    for j in range(n):
        for i in range(1,n):
            frecuencia_acum_mat[i][j]+=frecuencia_acum_mat[i-1][j]
    mensaje_generado=random.choice(alfabeto)
    
    for i in range(1,long_mensaje):
        num = random.random()
        cont=0
        j=alfabeto.index(mensaje_generado[i-1])
        while num> frecuencia_acum_mat[cont][j] and cont<n :
            cont+=1
        mensaje_generado +=alfabeto[cont]
        
      
    return mensaje_generado

def clasificacion_fuente(matt, tol=0.1):
    aux=[max(fila)-min(fila) for fila in matt]
    aux=max(aux)
    return (aux<tol)
mensaje="CAAACCAABAACBBCABACCAAABCBBACC"

mat,alfabet=a(mensaje)

mensaje=b(alfabet,mat,10)

if (clasificacion_fuente(mat)):
    print("Fuente de memoria nula")
    vec=Fuente_memoria_no_nula.Estacionario(mat,0.0001)
    print(f"Entropia: {Fuente_memoria_no_nula.Entropia_con_mem(mat,vec)}")
    
else:
    print("Fuente con memoria")
    vec=Fuente_memoria_no_nula.Estacionario(mat,0.0001)
    print(f"Entropia: {Fuente_memoria_no_nula.Entropia_con_mem(mat,vec):.2f}")
    
    

print("   " + "  ".join(alfabet))

# imprimir filas con su label
for i, fila in enumerate(mat):
    # formato con 2 decimales
    valores = "  ".join(f"{x:.2f}" for x in fila)
    print(f"{alfabet[i]}  {valores}")  
