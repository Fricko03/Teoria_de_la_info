import random
import copy
import math
def obtener_alfabeto_codigo(lista_pal_cod):
    
    alfa_cod=[]
    
    for i in lista_pal_cod:
        for j in i:
            if j not in alfa_cod:
                alfa_cod.append(j)
                
    return alfa_cod

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

def valor_W(w):
    
   prob=[w,1-w]
   info=saca_INFO_base_2(prob)
   
   return  entropia_base_2(prob,info)
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
    ordena = sorted(zip(alfabeto, probabilidades))
    alfabeto, probabilidades = map(list, zip(*ordena))
    
    return alfabeto,probabilidades


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



def obtener_longitudes_cod(lista_pal_cod):
    return [len(i)for i in lista_pal_cod]



def  entropia_base_r(lista_pal_cod,lista_probs):
    
    r=len(obtener_alfabeto_codigo(lista_pal_cod))
    info_fuente=obtener_info_base_r(lista_probs,r)
    
    return sum(s*p for s,p in zip(lista_probs,info_fuente))


def obtener_info_base_r(lista_probs,r):
    
    return [0 if i == 0 else math.log(1/i, r) for i in lista_probs]    



def longitud_media(lista_pal_cod,lista_probs):
    
    longitudes=obtener_longitudes_cod(lista_pal_cod)
    
    return sum(p*l for p,l in zip(longitudes,lista_probs))

#------------------------UNIDAD 5 -------------------------

    """Se normaliza la matriz dividiendo la fila por la suma de la misma 
    """
def normalizar_por_fila(matriz):

    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        if suma_fila != 0:
            for j in range(len(matriz[i])):
                matriz[i][j] /= suma_fila

    """
    
    Se obtienen los alfabetos de entrada y salida 
Luego creo una matriz donde cada celda [i][j] se acumula  
cuántas veces al ingresar ai(entrada) se obtuvo bj(salida).
Luego normalizo la matriz 
Devuelvo la matriz del canal P(b/a) 
    """
def mat_canal(entrada, salida):
    alf_entrada = sorted(list(set(entrada)))
    alf_salida = sorted(list(set(salida)))
    map_entrada = {simbolo: i for i, simbolo in enumerate(alf_entrada)}
    map_salida = {simbolo: i for i, simbolo in enumerate(alf_salida)}
    mat = [[0] * len(alf_salida) for _ in range(len(alf_entrada))]
    for i in range(len(entrada)):
        idx_entrada = map_entrada[entrada[i]]
        idx_salida = map_salida[salida[i]]
        mat[idx_entrada][idx_salida] += 1
    normalizar_por_fila(mat)
    return mat

    """se calcula la prob de salida en base a la formula sumatoria de P(ai)*P(bj/ai) uno por cada b iterando en a  tamaño(b)

    """
def Prob_de_b(probs_priori,probs_canal):
    probs_b=[0]*len(probs_canal[0])
    for j in range (len(probs_canal[0])):
        for i in range(len(probs_priori)):
            probs_b[j]+=probs_priori[i]*probs_canal[i][j]
    return probs_b
    """se calcula la prob posteriori de la siguiente forma p(ai/bj)=(P(bj/ai)*P(ai))/P(bj) obteniendo una  matriz de tamaño A*B
    """
def Prob_posteriori(probs_priori,probs_canal):
    mat=[[0] * len(probs_canal[0]) for _ in range(len(probs_priori))]
    probs_b=Prob_de_b(probs_priori,probs_canal)
    for i in range (len(probs_canal)):
        for j in range(len(probs_canal[0])):
            if (probs_b[j]!=0):
                mat[i][j]=(probs_canal[i][j]*probs_priori[i])/probs_b[j]
            else:
                mat[i][j]=0
   
    return mat
    """se calcula la prob simultanea de la siguiente formaP(ai,bi)=P(bj/ai)/P(ai)  obteniendo una  matriz de tamaño A*B
    """
def Prob_simultaneo(probs_priori,probs_canal):
     mat=[[0] * len(probs_canal[0]) for _ in range(len(probs_priori))]
     
     for i in range (len(probs_canal)):
        for j in range(len(probs_canal[0])):
            mat[i][j]=(probs_canal[i][j]*probs_priori[i])
     return mat


""" Es basicamente alcular una entropia por columna pero de la matriz de probabilidaes a posteriori=  sumatoria de P(a/bj)log(1/P(a/bj)) uno por cada b iterando en a, vector de tamaño(b)

"""
def entopia_posteriori(probs_priori,probs_canal):
    entropia=[]
    probs_posteriori=Prob_posteriori(probs_priori,probs_canal)
    for i in range(len(probs_posteriori[0])):
         columna = [fila[i] for fila in probs_posteriori]
         entropia.append(entropia_base_2(columna,saca_INFO_base_2(columna)))
    
    return entropia


    """ Primero se calcula la prob_simultanea y luego se utiliza en la siguiente formla para calcular la perdida, sumatoria de P(ai,bj)*log2(1/P(bj/ai))  iterando en a y b 
    """

def entropia_perdida(probs_priori,probs_canal):
    entropia =0
    
    prob_simultanea=Prob_simultaneo(probs_priori,probs_canal)
    # for i in range(len(mat)):
    #     entropia+=prob_salida[i]+entropi_post[i] 
    for i in range(len(probs_canal)):
        for j in range(len(probs_canal[0])):
            prob=prob_simultanea[i][j]
            if (probs_canal[i][j]!=0):
                entropia+=prob*math.log2(1/probs_canal[i][j])
            else:
                entropia+=0
         
    return entropia




    """Se calculan las prob dde salida y las entropias a  posteriori para usa en la siguiente formula sumatoria P(bj)*H(A/bj) iterando en b y sobre la entropía posteriori 

    """
def entropia_ruido(probs_priori,probs_canal):
    entropia =0
    entropia_post=entopia_posteriori(probs_priori,probs_canal)
    prob_salida=Prob_de_b(probs_priori,probs_canal)
   
    for i in range(len(probs_canal[0])):
        entropia+=prob_salida[i]*entropia_post[i] 

    return entropia

""" Primero se calcula la prob_simultanea y luego se utiliza en la siguiente formla para calcular la perdida, sumatoria de P(ai,bi)*log)1/P(ai,bi) iterando en a y b 
"""

def entropia_afin(prob_a_priori,mat_canal):
    prob_simultanea=Prob_simultaneo(prob_a_priori,mat_canal)
    entropia=0
    for i in range(len(mat_canal)):
        for j in range(len(mat_canal[0])):
            prob=prob_simultanea[i][j]
            if (prob!=0):
                entropia+=prob*math.log2(1/prob )
            else:
                entropia+=0

           
    
    return entropia

"""se calcula la info mutua usando estas formula   H(A)-H(A/B)
"""

def info_mutua_a_b(probs_priori,probs_canal):
    entropia_entrada=entropia_base_2(probs_priori,saca_INFO_base_2(probs_priori))
    entropia_ruidosa=entropia_ruido(probs_priori,probs_canal)
    
    
    
    return entropia_entrada-entropia_ruidosa

"""se calcula la info mutua usando estas formula   H(B)-H(B/A)
"""
def info_mutua_b_a(probs_priori,probs_canal):
    probs_b=Prob_de_b(probs_priori,probs_canal)
    entropia_salida=entropia_base_2(probs_b,saca_INFO_base_2(probs_b))
    entropia_perdidosa=entropia_perdida(probs_priori,probs_canal)
    
    
    
    return entropia_salida-entropia_perdidosa


"""se calcula la info mutua usando esta formula   sumatoria P(ai,bj)*log2(P(ai/bj)/P(ai)) iterando en a y 
"""
def entropia_priori(probs_priori):
    return entropia_base_2(probs_priori,saca_INFO_base_2(probs_priori))

"""Entropia clasica con los elementos de salida sumatoria de p(b)*log2(1/p(b))"""
def entropia_salida(probs_priori,probs_canal):
    probs_sal=Prob_de_b(probs_priori,probs_canal)
    return entropia_base_2(probs_sal,saca_INFO_base_2(probs_sal))   


#-----------------UNIDAD 6 --------------------------------
    """Revisa la matriz del canal columna por columna. Si encuentra una columna (un símbolo de salida) que puede ser generada por más de una fila (más de un símbolo de entrada),
    significa que el canal es "ruidoso" (hay pérdida de información) y devuelve False. Si todas las salidas provienen de una única entrada, devuelve True.
    """

def is_not_ruidosa(probs_canal):
    
    for j in range (len(probs_canal[0])):
        cont=0
        for i in range(len(probs_canal)):
            if probs_canal[i][j] !=0:
                cont+=1
            if cont>1:
                return False
    

    return True
"""Revisa la matriz del canal fila por fila. 
Si encuentra una fila (un símbolo de entrada) que puede generar más de una columna (más de un símbolo de salida), 
significa que el canal no es determinista y devuelve False. Si cada entrada produce una única salida, devuelve True."""
def is_determinante(probs_canal):
        
    for i in range (len(probs_canal)):
        cont=0
        for j in range(len(probs_canal[0])):
            if probs_canal[i][j] !=0:
                cont+=1
            if cont>1:
                return False
    

    return True

    """Para calcular la matriz resultante de un canal en serie se calcula la Calcula la multiplicación de matrices estándar entre probs_canal_1 y probs_canal_2.
    
    """
def mat_compuesta(probs_canal_1,probs_canal_2):
    mat_compuesta=[[0]*len(probs_canal_2[0]) for _ in range(len(probs_canal_1))]
    for i in range(len(probs_canal_1)):
        for j in range(len(probs_canal_2[0])):
            for k in range(len(probs_canal_2)):
                mat_compuesta[i][j]+=probs_canal_1[i][k]*probs_canal_2[k][j]
    return mat_compuesta


   
    """Comprueba si dos columnas de la matriz (indicadas por los índices j1 y j2) 
    son linealmente dependientes. Es decir, verifica si una columna es simplemente un múltiplo constante de la otra (ej: Columna 1 = 0.5 * Columna 2). Devuelve True si lo son, False si no.
    """
def is_lineal(mat_canal,j1,j2):
    #verifica
   
    
    
    columna1=[fila[j1] for fila in mat_canal]
    columna2=[fila[j2] for fila in mat_canal]
    constantes=[]
    for e1, e2 in zip(columna1, columna2):
    
    # 1. Ambos son distintos de cero -> División
        if e1 != 0 and e2 != 0:
            constantes.append(e1 / e2)
            
        # 2. Ambos son cero -> Ignorar 
        elif not(e1 == 0 and e2 == 0):
        
            return False
        
    encontre_prim=False

    for i in range(len(constantes)):
       
        if (encontre_prim and constantes[i]!=c):
            return False
        elif not (encontre_prim):
            c=constantes[i]
            encontre_prim=True


    return True

    """Se genera un amatriz identidad de tamaño B*B y se "suman" las columnas c1 y c2 eliminando c2 
    """
def genera_mat_det(mat,c1,c2):
    mat_compuesta = [[1 if i==j else 0 for j in range(len (mat[0]))] for i in range(len(mat[0]))]
    for fila in mat_compuesta:
        fila[c1] += fila[c2]
    
    # Elimina la columna c2
    for fila in mat_compuesta:
        fila.pop(c2)
    return mat_compuesta


        
def imprimir_matriz_normal(M):
    for fila in M:
        print(fila)


    """Recorre todos los pares de columnas posibles de la matriz. Usa la función is_lineal para comprobar si algún par es linealmente dependiente.
    Si encuentra un par, devuelve sus índices (i, j). Si revisa todos los pares y ninguno lo es, devuelve (-1, -1).
    """
def se_puede_reducir(mat):
    for i in range(len(mat[0])):
        for j in range(i+1,len(mat[0])):
            if is_lineal(mat,i,j):
                return i,j
    return -1,-1
    """Reduce la matriz del canal tanto como sea posible. Primero, busca un par de columnas reducibles (con se_puede_reducir). 
    Si las encuentra, genera la matriz de fusión (con genera_mat_det) y calcula el nuevo canal reducido (con mat_compuesta). 
    Repite este proceso en bucle hasta que no queden más columnas por fusionar.
    """
def genera_matriz_canal_reducido(mat,prob):
    i,j=se_puede_reducir(mat)
    # print("Info mutua original ",info_mutua_a_b(prob,mat))
    mat2=mat
    while i!=-1:
        mat_determinante = genera_mat_det(mat2,i,j)
        mat2=mat_compuesta(mat2,mat_determinante)
        # imprimir_matriz_normal(mat2)
        
        # print("Info mutua ",info_mutua_a_b(prob,mat2))
        
        i,j=se_puede_reducir(mat2)
        
    return mat2

"""Verifica si el canal es uniforme (o débilmente simétrico). Lo hace comprobando si todas las filas son permutaciones unas de otras. 
Es decir, si ordenas los números de cada fila, todas las filas ordenadas deben ser idénticas"""
def is_uniforme(matriz_canal):
   
    num_filas = len(matriz_canal)
    if num_filas <= 1:
        return True
    fila_referencia_ordenada = sorted(matriz_canal[0])
    for i in range(1, num_filas):
        fila_actual = matriz_canal[i]
        fila_actual_ordenada = sorted(fila_actual)
        if fila_actual_ordenada != fila_referencia_ordenada:
            return False
    return True
"""Calcula la capacidad del canal (la máxima información mutua). Utiliza fórmulas directas y eficientes si detecta que el canal es de un tipo especial: determinista, no ruidoso o uniforme."""
def calcula_capacidad(mat_canal):
    capacidad=0
    if (is_determinante(mat_canal)):
        capacidad=math.log2(len(mat_canal[0]))
    elif (is_not_ruidosa(mat_canal)):
        capacidad=math.log2(len(mat_canal))
    elif (is_uniforme(mat_canal)):
        i=0
    
        for j in range(len(mat_canal[0])):
            
            if (mat_canal[i][j]!=0):
                capacidad-=mat_canal[i][j]*math.log2(1/mat_canal[i][j])
            else:
                capacidad=0
        capacidad+=math.log2(len(mat_canal[0]))
    return capacidad
"""Calcula la capacidad de un canal binario (2 entradas). Lo hace probando muchas distribuciones de probabilidad de entrada (ej: [0.1, 0.9], [0.2, 0.8], etc., según el paso).
Calcula la información mutua para cada una y devuelve el valor máximo que encontró (la capacidad) y la probabilidad de entrada que la produjo."""

def capacidad_binaria(mat_canal,paso):
    mutua=[]
    WES=[]
    i=0
    while(i<=1):
        
        prob_priori=[i,1-i]
        mutua.append(info_mutua_a_b(prob_priori,mat_canal))
        WES.append(i)
        i+=paso
    return max(mutua),WES[mutua.index(max(mutua))]

# devuelve I(max) y W
def calcula_error(probs_priori,mat_canal):
    prob_error=0
    matriz_copia = [fila[:] for fila in mat_canal]
    
    for i in range (len(mat_canal[0])):
        columna = [fila [i] for fila in mat_canal]
        matriz_copia[columna.index(max(columna))][i]=0
    for i in range(len(matriz_copia)):
            prob_error+=probs_priori[i]*sum(matriz_copia[i])
    return prob_error



def decodificar_y_corregir_paridad(mensaje_codificado_bytes):
   
    

    mensaje_original = ""
    matriz_recibida = []
    for byte_val in mensaje_codificado_bytes:
       
        bits = [int(b) for b in bin(byte_val)[2:].zfill(8)]
        matriz_recibida.append(bits)
    
    # Se suman los bits de paridad vertical (columna 7) de las filas de datos (desde la fila 1)
    suma_col = sum(matriz_recibida[i][7] for i in range(len(matriz_recibida)))
 
    if sum(matriz_recibida[0])%2!=0 or (suma_col%2!=0 ):
        print("Error en pariedad cruzada se descarta el mensaje por protocolo de paridad.")
    else:
        filas_con_error = []
        cols_con_error = [] 
        for i in range(len(matriz_recibida)):
            
            paridad_recibida = matriz_recibida[i][7]
            total_unos = sum(matriz_recibida[i][:7])
            lpc_calculado = 1 if total_unos % 2 != 0 else 0
            
            if lpc_calculado != paridad_recibida:
                filas_con_error.append(i)

    
        for j in range(8):
            
            paridad_recibida = matriz_recibida[0][j]
            total_unos = sum(matriz_recibida[i][j] for i in range(1, len(matriz_recibida)))
            vpc_calculado = 1 if total_unos % 2 != 0 else 0
            if vpc_calculado != paridad_recibida:
                cols_con_error.append(j)

        
        
        if len(filas_con_error) == 1 and len(cols_con_error) == 1:
            fila_err = filas_con_error[0]
            col_err = cols_con_error[0]

            matriz_recibida[fila_err][col_err] ^= 1
            print("Error único detectado y corregido.")

        elif len(filas_con_error) == 0 and len(cols_con_error) == 0:
            pass # No se hace nada, el mensaje se acepta tal cual.
            
        
        else:

            print("Error múltiple o no localizable. Mensaje descartado.")
            return "" # Devolver cadena vacía
        
        for i in range(1, len(matriz_recibida)):
            # Tomar los 7 bits de datos
            bits_datos = matriz_recibida[i][:7]
            bin_str = "".join(map(str, bits_datos))
            mensaje_original+=chr(int(bin_str, 2))
                
                
        
    return mensaje_original
def paridad_caracter(carat):#par
    
    ascii_val = ord(carat)
    cant_unos = ascii_val.bit_count()
    if cant_unos%2==0:
        ascii_val=ascii_val<<1
    else:
        ascii_val=ascii_val<<1|1
    return ascii_val
"""
    Verifica si el bit de pariedad ya que 
    al agregar el bit de pariedad si era impar se agrega un 1 y lo hace par y se era para aguega un 0 por ende sigue siendo par 
    entonces lo que se verifica es que la cantidad de unos sea par en caso contrario la pariedad esta mal 
"""
def verificacion(byte):
    total_de_unos = byte.bit_count()
    if total_de_unos % 2 == 0:
         return True  # La regla (TOTAL PAR) se cumplió. Todo bien.
    else:
        return False # La regla (TOTAL PAR) se ROMPIÓ. Hubo error.

Entrada=	"10011111101000101000101110110100"
Salida=	"LKKMKMLLKKMJJKJKKKKJKKJMJKKKJLJK"


print("----------Punto A--------------")
alf,prob_priorii=Alfabeto_y_sus_probabilidades(Entrada)
print("Las probabilidades a priori son: ", prob_priorii)
ma_canal=mat_canal(Entrada,Salida)
print("La matriz del canal es: ")
imprimir_matriz_normal(ma_canal)

print("----------Punto B--------------")
if is_not_ruidosa(ma_canal):
    print("Es un canal con sin ruido")
else :
    print("Es un canal con ruido")
    
if is_determinante(ma_canal):
    print("Es un canal determinante")
else :
    print("No es un canal determinante")
    
    
print("----------Punto C--------------")

equivocacion=entropia_ruido(prob_priorii,ma_canal)
perdida=entropia_perdida(prob_priorii,ma_canal)
info_mutu=info_mutua_a_b(prob_priorii,ma_canal)
print("La equivocacion es: ", equivocacion)
print("La perdida es: ", perdida)
print("La info mutua es: ", info_mutu)

print("----------Punto d--------------")

mat_reducida=genera_matriz_canal_reducido(ma_canal,prob_priorii)
imprimir_matriz_normal(mat_reducida)

print("----------Punto E--------------")

capa_bin,w=capacidad_binaria(ma_canal,0.0001)
print("La capacidad del canal binario es: ", capa_bin)
print("P(0)= ",w)
print("P(1)= ",1-w )

prob_error=calcula_error(prob_priorii,ma_canal)
print("La probabilidad de error es: ", prob_error)

print("----------Punto F--------------")
mat_pari=["10011111",
          "10100010",
          "10001011",
          "10110100",
    
]
mansaje=bytearray()
for fila in mat_pari:
        
        byte_val = int(fila, 2)
        
        mansaje.append(byte_val)
mensaje=decodificar_y_corregir_paridad(mansaje)
print("El mensaje es: ",mensaje)

print("----------Punto G--------------")