import math

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
def Entropia_con_mem(mat_transicion,vec_esta):
    suma=[]
    
    num_filas = len(mat_transicion)
    num_columnas = len(mat_transicion[0])
    for i in range(num_columnas):
        columna = [fila[i] for fila in mat_transicion]
        suma.append(entropia_base_2(columna,saca_INFO_base_2(columna))*vec_esta[i])    #en caso de tener que calcular la entropia en otra base cambiar    
    return sum(suma)
def saca_INFO_base_2(probs):
    resultado=[]
    for s in probs:
        if(s==0):
            resultado.append(0)
        else:
            resultado.append(math.log2(1/s))
    return  resultado

def entropia_base_2(lista_pro,lista_INFO):
   return  sum(s*p for s,p in zip(lista_pro,lista_INFO))

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

def normalizar(matriz):
  
    filas = len(matriz)
    columnas = len(matriz[0])

    # recorremos columnas
    for j in range(columnas):
        suma = sum(matriz[i][j] for i in range(filas))  # suma de la columna j
        if suma != 0:
            for i in range(filas):
                if (suma!=0):
                    matriz[i][j] /= suma
    

def imprime_mat(alfabet,matt):      
    print("   " + "       ".join(alfabet))

    # imprimir filas con su label
    for i, fila in enumerate(matt):
        # formato con 2 decimales
        valores = "  ".join(f"{x:.2f}" for x in fila)
        print(f"{alfabet[i]}  {valores}") 
        
        
        
def Estacionario(mat_trans,tol):
    estacionario_prev=[1/len(mat_trans)]
    estacionario_prev*=len(mat_trans) #creo el v0 que es todos sus elementos equisprobables
    vec_estacionario=[] #creo el que voy a usar en las iteraciones
    
    if (columnas_suman_1(mat_trans)):
    #genero el primer v1 en base a v0
        for i in range(len(mat_trans)):
            suma=0
            for j in range(len(mat_trans[0])):
                suma+=estacionario_prev[j]*mat_trans[i][j]
            vec_estacionario.append(suma)
        
    
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


def is_mem_nula(matt, tol=0.1):
    aux=[max(fila)-min(fila) for fila in matt]
    aux=max(aux)
   
    return aux<tol



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



mensaje1="+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"
##------------punto a---------------

alfabeto,probabilidades=Alfabeto_y_sus_probabilidades(mensaje1)
ordena = sorted(zip(alfabeto, probabilidades))
alfabeto, probabilidades = map(list, zip(*ordena))
print(f"El alfabeto del mensaje 1 es: {alfabeto} y sos probabilidades son las siguientes:")
for i,prob in enumerate(probabilidades):
    print(f"Simbolo {alfabeto[i]} probabilidad {prob:.2}")
    
##------------punto b---------------

matriz_transicion,_=alfabeto_mat_con_mem(mensaje1)

imprime_mat(alfabeto,matriz_transicion)
##------------punto c---------------

if is_mem_nula(matriz_transicion):
    alf,probs=Alfabeto_y_sus_probabilidades(mensaje1)
   
    print(f"La fuente que origino ese mensaje es una fuente de memoria nula" )
else:
   
    print(f"La fuente que origino ese mensaje es una fuente con memoria")

##------------punto d---------------
##la fuente es de memoria nula

informacion=saca_INFO_base_2(probabilidades)
entropia=entropia_base_2(probabilidades,informacion)
print(f"La entropia de la fuente es : {entropia:.2f}")


##------------punto e---------------
alfabeto_extendido,probabilidades_entendidas=calc_exte(alfabeto,probabilidades,2)

print(f"El alfabeto extendido es: {alfabeto_extendido} y sos probabilidades son las siguientes:")
for i,prob in enumerate(probabilidades_entendidas):
    print(f"Simbolo {alfabeto_extendido[i]} probabilidad {prob:.2}")

informacion_extendida=saca_INFO_base_2(probabilidades_entendidas)
entropia_extendida=entropia_base_2(probabilidades_entendidas,informacion_extendida)
print(f"La entropia de la fuente es : {entropia_extendida:.2f}")


print("ACA COMIENZA LA PREGUNTA 2")
print()
print()
print()
mensaje1="]]]([[]))([(])]([]([([([)([([([[([))][([([[([)([(]"
##------------punto a---------------

alfabeto,probabilidades=Alfabeto_y_sus_probabilidades(mensaje1)
ordena = sorted(zip(alfabeto, probabilidades))
alfabeto, probabilidades = map(list, zip(*ordena))
print(f"El alfabeto del mensaje 1 es: {alfabeto} y sos probabilidades son las siguientes:")
for i,prob in enumerate(probabilidades):
    print(f"Simbolo {alfabeto[i]} probabilidad {prob:.2}")
    
##------------punto b---------------

matriz_transicion2,_=alfabeto_mat_con_mem(mensaje1)

imprime_mat(alfabeto,matriz_transicion2)
##------------punto c---------------

if is_mem_nula(matriz_transicion2):
    alf,probs=Alfabeto_y_sus_probabilidades(mensaje1)
   
    print(f"La fuente que origino ese mensaje es una fuente de memoria nula" )
else:
   
    print(f"La fuente que origino ese mensaje es una fuente con memoria")

# ##------------punto f y d---------------
# ##la fuente es de memoria no nula

vector_estacionario=Estacionario(matriz_transicion2,0.001)
entropia=Entropia_con_mem(matriz_transicion2,vector_estacionario)
print("El vector estacionario es:" )

for i in (vector_estacionario):
    print(f"{i:.2}")
print(f"La entropia de la fuente es : {entropia:.2f}")


