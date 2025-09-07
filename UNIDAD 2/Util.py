#Importacion de librerias
import random
import copy
import math

#FUENTE SIN MEMORIA

def valor_W(w):
   prob=[w,1-w]
   info=saca_INFO(prob)
   return  entropia(prob,info)
#SACAR ALFABETO PROB
def Alfabeto_y_sus_probabilidades(mensaje):
    alfabeto=[]
    probabilidades=[]
    for c in mensaje:
        if (c not in alfabeto):
            alfabeto.append(c)
            probabilidades.append(1)
        else:
            probabilidades[alfabeto.index(c)] += 1
    
    probabilidades=[i/len(mensaje) for i in probabilidades]
    return alfabeto,probabilidades
        

#GENERAR MENSAJE EN BASE A UN ALFABEJO Y SUS PROBABILIDADES

def Generador_mensaje(alfabeto,probabilidades,n):
    frecuencia_acum=[]
    frecuencia_acum.append(probabilidades[0])
    for i in range(1,len(probabilidades)):
        frecuencia_acum.append(probabilidades[i]+frecuencia_acum[i-1])
    print(frecuencia_acum)
    mensaje_generado=""
    
    for i in range(n):
        num = random.random()
        cont=0
        while num> frecuencia_acum[cont]:
            cont+=1
        mensaje_generado +=alfabeto[cont]
      
    return mensaje_generado

#####################################

def saca_INFO(probs):
    resultado=[]
    for s in probs:
        if(s==0):
            resultado.append(0)
        else:
            resultado.append(math.log2(1/s))
    return  resultado

def entropia(lista_pro,lista_INFO):
   return  sum(s*p for s,p in zip(lista_pro,lista_INFO))

###################

#FUENTE SIN MEMORIA EXTENDIDA
    #GENERA ALFABETO EXTENDIDO Y PROBABILIDADES EXTENDIDAS
def calc_exte(alfabeto,probabilidades,n):
    if (n==1):
        return alfabeto,probabilidades
    else:
        alfabeto_extendido,probablilidades_extendido=calc_exte(alfabeto,probabilidades,n-1)
        alfabeto_extendido=alfabeto_extendido*len(alfabeto)
        
        probablilidades_extendido=probablilidades_extendido*len(probabilidades)
        
        alfabeto_aux=[letra for letra in alfabeto for i in range(len(alfabeto)**(n-1))]
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
                
                alfabeto_extendido[j]=letra+alfabeto_extendido[j]
                probablilidades_extendido[j]=probabilidades[i]*probablilidades_extendido[j]
          fin+=len(alfabeto)**(n-1)
         
              
    return alfabeto_extendido,probablilidades_extendido

####################################################
## FUENTE CON MEMORIA

    #CALCULA EL VECTOR ESTACIONARIO
def Estacionario(mat_trans,tol):
    estacionario_prev=[1/len(mat_trans)]
    estacionario_prev*=len(mat_trans)
    vec_estacionario=[]
  
    #genero el primer v1
    for i in range(len(mat_trans)):
        suma=0
        for j in range(len(mat_trans[0])):
            suma+=estacionario_prev[j]*mat_trans[i][j]
        vec_estacionario.append(suma)
    
    if (columnas_suman_1(mat_trans)):
        while(diferencia(estacionario_prev,vec_estacionario)>tol):
            estacionario_prev=vec_estacionario[:]
            for i in range(len(mat_trans)):
                suma=0
                for j in range(len(mat_trans[0])):
                    suma+=estacionario_prev[j]*mat_trans[i][j]
                vec_estacionario[i]=suma
    else:
        print("La matriz de transicion esta mal hecha")

    return vec_estacionario

#VERIFICO QUE LAS COLUMNAS SUMEN 1    
def columnas_suman_1(M, tol=1e-8):
  
    num_filas = len(M)
    num_columnas = len(M[0])
    
    for j in range(num_columnas):        
        suma = 0
        for i in range(num_filas):       
            suma += M[i][j]
        if abs(suma - 1) > tol:         
            return False
    return True

#CALCULA LA DIFERENCIA ENTRE LOS VEC ESTACIONARIOS
def diferencia(vp,va):
    aux=[]
    for i in range(len(vp)):
        aux.append(abs(vp[i]-va[i]))
    return max(aux)

#CALCULO DE ENTROPIA CON MEMORIA SUM(V*H(M))
def Entropia_con_mem(mat_transicion,vec_esta):
    suma=[]
    
    num_filas = len(mat_transicion)
    num_columnas = len(mat_transicion[0])
    for i in range(num_columnas):
        columna = [fila[i] for fila in mat_transicion]
        suma.append(entropia(columna,saca_INFO(columna))*vec_esta[i])    
    
    return sum(suma)


#CALCULA MATRIZ DE TRANSICION Y PROBS EN BASE A UN STR
def alfabeto_mat_con_mem(mensaje):
    
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

#dividimos cada m[i][j] por la sum[j]
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
    
def Generador_mensaje_con_mem(alfabeto,mat_fun,long_mensaje):
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
    

    if ((aux<tol)):
        print("Fuente de memoria nula")
        vec=Estacionario(matt,0.0001)
        print(f"Entropia: {Entropia_con_mem(matt,vec)}")
        
    else:
        print("Fuente con memoria")
        vec=Estacionario(matt,0.0001)
        print(f"Entropia: {Entropia_con_mem(matt,vec):.2f}")

def imprime_mat(alfabet,matt):      
    print("   " + "  ".join(alfabet))

    # imprimir filas con su label
    for i, fila in enumerate(matt):
        # formato con 2 decimales
        valores = "  ".join(f"{x:.2f}" for x in fila)
        print(f"{alfabet[i]}  {valores}") 