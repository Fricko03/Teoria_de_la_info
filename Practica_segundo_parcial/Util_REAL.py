#Importacion de librerias

from ast import Return
import random
import copy
import math




#FUENTE SIN MEMORIA



#GENERAR MENSAJE EN BASE A UN ALFABEHO Y SUS PROBABILIDADES

def Generador_mensaje(alfabeto,probabilidades,n):
    frecuencia_acum=[]
    frecuencia_acum.append(probabilidades[0])
    for i in range(1,len(probabilidades)):
        frecuencia_acum.append(probabilidades[i]+frecuencia_acum[i-1]) #aca lo que hago es calcular la frec acum
    print(frecuencia_acum) #print innecesario 
    mensaje_generado=""
    
    for i in range(n):#bucle de 0 a n que se relaciona con el largo del msm
        num = random.random()
        cont=0
        while cont < len(frecuencia_acum)-1 and num> frecuencia_acum[cont]:
            cont+=1
        mensaje_generado +=alfabeto[cont]
      
    return mensaje_generado

#####################################

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



####################################################
## FUENTE CON MEMORIA

    #CALCULA EL VECTOR ESTACIONARIO
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

#CALCULO DE ENTROPIA CON MEMORIA SUM(V*H(M))
def Entropia_con_mem(mat_transicion,vec_esta):
    suma=[]
    
    num_filas = len(mat_transicion)
    num_columnas = len(mat_transicion[0])
    for i in range(num_columnas):
        columna = [fila[i] for fila in mat_transicion]
        suma.append(entropia_base_2(columna,saca_INFO_base_2(columna))*vec_esta[i])    #en caso de tener que calcular la entropia en otra base cambiar    
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
                if (suma!=0):
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
        while cont<n-1 and num> frecuencia_acum_mat[cont][j]:
            cont+=1
        mensaje_generado +=alfabeto[cont]
        
      
    return mensaje_generado

def is_mem_nula(matt, tol=0.1):
    aux=[max(fila)-min(fila) for fila in matt]
    aux=max(aux)
   
    return aux<tol

def imprime_mat(alfabet,matt):      
    print("   " + "  ".join(alfabet))

    # imprimir filas con su label
    for i, fila in enumerate(matt):
        # formato con 2 decimales
        valores = "  ".join(f"{x:.2f}" for x in fila)
        print(f"{alfabet[i]}  {valores}") 
        
        
def es_no_singular(C1):
    s1=set(C1)
    return len(C1)==len(s1)

def es_instantaneo(C1):
    # if (es_no_singular(C1)):[]
        for k,i in enumerate(C1):
            for j in range(len(C1)):
                if (k!=j and C1[j].startswith(i)):
                    return False
        return True
    # else:
    #     return False


def es_UD(C1): ## preguntar antes si es no singular
    lista_de_S=[]
    C1=set(C1)
    s1=set(C1)
    s_aux=set()
    lista_de_S.append(s1)
    for i in s1:
        for j in C1:
            if (j!=i):
                if (j.startswith(i)):
                    s_aux.add(j[len(i):])
                elif (i.startswith(j)):
                    s_aux.add(i[len(j):])
    while( not C1.intersection(s_aux) and  s_aux not in lista_de_S):
        lista_de_S.append(s_aux.copy())
        s_aux.clear()    
        for i in lista_de_S[-1]:
            for j in s1:
                if (j!=i):
                    if (j.startswith(i)):
                        s_aux.add(j[len(i):])
                    elif (i.startswith(j)):
                        s_aux.add(i[len(j):])
    
    return s_aux in lista_de_S
def propiedades(C1):
    if (es_no_singular(C1)):
        if(es_UD(C1)):
            if(es_instantaneo(C1)):
                print("Es instantaneo")
            else:
                print("Es Univocamente decodificable") 
        else:
            print("Es no singular")
    else:
        print("Es bloque")





def is_compacto(lista_pal_cod,lista_probs):
    if (es_instantaneo(lista_pal_cod)):
        lista_info=obtener_info_base_r(lista_probs,len(obtener_alfabeto_codigo(lista_pal_cod)))
        longitudes=obtener_longitudes_cod(lista_pal_cod)
        i=0
        while (i<len(lista_pal_cod) and longitudes[i]<=math.ceil( lista_info[i])):
            # print(longitudes[i],math.ceil(lista_info[i]))
            i+=1
    else:
        i=0
    return  i==len(lista_pal_cod)    

def Generador_mensaje_en_base_alfabeto_cod(alfabeto_cod,probabilidades,n):
    frecuencia_acum=[]
    frecuencia_acum.append(probabilidades[0])
    for i in range(1,len(probabilidades)):
        frecuencia_acum.append(probabilidades[i]+frecuencia_acum[i-1])
    print(frecuencia_acum)
    mensaje_generado=""
    
    for i in range(n):
        num = random.random()
        cont=0
        while cont < len(frecuencia_acum)-1 and num> frecuencia_acum[cont]:
            cont+=1
        mensaje_generado +=alfabeto_cod[cont]
      
    return mensaje_generado

def calcula_kraf_en_base_tam(tamanios,r):
    #r es el tamanio del alfabeto codigo
    
    return sum((r ** (-l) for l in tamanios))
    
    
def sum_ine_kraft(lista_pal_cod):
    r=len(obtener_alfabeto_codigo(lista_pal_cod))
    longitudes=obtener_longitudes_cod(lista_pal_cod)
    suma= [r**(-i) for i in longitudes]
    return sum(suma)

# ---------------------------------------SEGUNDO PARCIAL----------------------------------------------------
    
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

#---------------------Utiless---------------------------------


""" 

en el primer teoriema de Shannon surgue de la primicia de que la entropia hace de cota inferior para la 
longitu media ya que si la longitud media fuera menor a esta, estariamos frente a un caso en el cual se perdio informacion 
se demuestra la formula del teorema de shannon 
primero se calcula la extension del codigo, despues la logitud media de la extension y la entropia en base r(que siempre es dos en la materi
pero aca esta hecho generico )
luego se verifica la expresion Hr(S)<=Ln/n<Hr(s)+1/n
"""
#ver si debo extender el codigo de codificacion antes de hacerlo 
#se mandan las probabilidades originales
def primerteoremaShanon(probabilidad,codigoextendido,N):
    
    alfabeto_vacio=[""]*len(probabilidad)
    _,probexte=extendida_bien(alfabeto_vacio,probabilidad,N)
    longitud=longitud_media(codigoextendido,probexte)
    entropia=entropia_base_r(codigoextendido,probabilidad)
    
    print("Longitud",longitud)
    print("Entropia",entropia)
    print(entropia,"<=",longitud/N,"<=",(entropia+1/N))
    
    return entropia<=longitud/N<=(entropia+1/N)

"""se efectua el calculo de la redundancia y rendimiento en base a la formula
Rendimiento eficiencia: n=Hr(S)/Ln Redundancia:1-n=(L-Hr(S))/L
el rendimiento es maximo si L=H   
queda en evidencia que si reducimos l/n mucho aumenta la complejidad 
mayor redundancia menor infromacion 
"""
def calculo_redundancia_rendimiento(probabilidades,codificacion):
    
    entropia=entropia_base_r(codificacion,probabilidades)
    logitud=longitud_media(codificacion,probabilidades)
    
    return entropia/logitud,(1-entropia/logitud)


    """primero creo una lista itemsque  almacena la probabilidad y una lista de los indices del simbolo al que pertenece 
luego se ordena la lista de mayor a menor,mediante una funcion lambda,  de manera que los de menor probabilidad queden al final-
se sacan los dos ultimos elementos de a uno con pop, y se los almacena en dos listas con el mismo formato que items,  
Luego a todos los simbolos del elemento con menor  probabilidad se les agrega un 0 a la izquierda
y a todos los del segundo menor se les agrga un 1 en la lista codigos mediante los indices almacenadis 
Para finalizar se combinan los dos simbolos sumando sus probabilidades  y concatenando indices 
se vuelven a agregar a la lista y esto  se repite hasta que quede un elemento en la lista 
    """
def huffman_binario(probs):
    
    items = [[p, [i]] for i, p in enumerate(probs)]
    codigos = [''] * len(probs)
    
    if len(items)==1:
        
        return ["0"]
    
    while len(items)>1:
        
        items = sorted(items, key=lambda x: x[0],reverse=True)
        menor_1=items.pop()
        menor_2=items.pop()
        
        for i in menor_1[1]:
            codigos[i] = '0' + codigos[i]
        
        for i in menor_2[1]:
            codigos[i] = '1' + codigos[i]
            
        items.append([menor_2[0]+menor_1[0],menor_1[1]+menor_2[1]])

    return codigos

"""
primero se crea una lista de elementos donde cada uno contiene la probabilidad y el indice del simbolo
luego se ordena de mayor a menor con una funcion lambda 
y se llama a la funcion _shanon_rec_bin, la cual va dividiendo la lista en dos conjuntos de probabilidades recursivamente 
dividiendo esta lo mas cerca a la mitad(disponible) o haciendo que la diferencia de las probabilidades entre los dos subconjuntos minima, para lograr eso 
en cada llamada recursiva se calcula, primero la suma total de las probabilidades del conjunto a dividir, que en la primera iteracion seria 0.5 pero luego puede variar dependiendo de donde se dividio el punto anterior,
la suma  de las probabilidades hasta que se pasa de la mitad de la suuma total de las probabilidades
luego se busca el punto donde la suma acumulada supera la mitad del total. Segun este resultado se decide para donde va el elemento compartido
A todos los simbolos del conjunto1 se les agrega un uno a la derecha 
y los del conjunto0 un 0.
Finalmente se llama recursivamente con ambos conjuntos, hasta que quede un único elemento.
El resultado final es un código Shannon-Fano para cada símbolo  
"""
def _shanon_rec_bin(items, cods):
    
    n=len(items)
     
    if(n>1):
        
        prob_tot=sum(i[0] for i in items)
        acum=0
        resto=0
        i=0
        
        while (i<=n-1 and acum<prob_tot/2):
            acum+=items[i][0]
            i+=1
            
        for j in range(i-1,n):
            resto+=items[j][0]

        if acum>resto:
            i=i-1
            
        cod_1= items[0:i]
        cod_0=items[i:]
        
        for j in cod_0:
            cods[j[1]]=cods[j[1]]+'0'
           
        for j in cod_1:
            cods[j[1]]=cods[j[1]]+'1'
           
        _shanon_rec_bin(cod_0,cods)
        _shanon_rec_bin(cod_1,cods)
    
def shanon_binario(probs):
    
    items = [[p, i] for i, p in enumerate(probs)]
    codigos = [''] * len(probs)
    items = sorted(items, key=lambda x: x[0],reverse=True)
    _shanon_rec_bin(items,codigos)
    
    return codigos


"""
Dada una cadena de caracteres con un mensaje escrito en el alfabeto fuente,
devolver una secuencia de bytes (bytearray) que contenga el mensaje codificado
mediante un diccionario toma caracter a carater del mensaje y devuelve la codificacion correspondiente concatenandolas 
hasta codificar todo el mensaje
luego evaluo cuanto de resto debo agregar para que entre los bits del mensaje, los bits que me indica el resto y el resto sea multiplo de 8
una vez terminado este paso se toman de a 8 y se conbierte a int para almacenad en el bytearray cadena que almacena el mensaje codificado 
   """
    
    
def codificacion_binaria(alfabeto_fuente, codificacion, mensaje):
    
    cadena = bytearray()
    cadena_str = "" 
    dicionario_codificacion = dict(zip(alfabeto_fuente, codificacion))
    
    for i in mensaje:
        cadena_str += dicionario_codificacion[i]
        
    # Calcular el 'resto' necesario para que el total de bits de datos + resto
    # sea múltiplo de 8, dejando espacio para 1 byte (8 bits) del marcador de 'resto'.
    # La nueva fórmula es: (8 - (len(cadena_str) + 8) % 8) % 8
    # En esencia, queremos que len(cadena_str) + 8 + resto sea un múltiplo de 8.
    resto = (8 - (len(cadena_str) + 8) % 8) % 8
    
    if resto != 0:
        cadena_str += "0" * resto
        
    resto_binario = bin(resto)[2:].zfill(8)
    cadena_str = resto_binario + cadena_str
    
    for i in range(0, len(cadena_str), 8):
        # Tomar bloques de 8 bits y convertirlos a un entero, luego agregarlo al bytearray
        cadena.append(int(cadena_str[i:i+8], 2))
        
    return cadena 


"""
  Reconstruye el mensaje original a partir de los bytes codificados.
Primero convierto cada byte en su representacion de 8 bits en string 
Los primeros 8 bits indican cuántos ceros adicionales fueron agregados por el resto 
en la codificacion, por lo que se extrae ese valor y se eliminan esos ceros del final de la cadena
Para decodificar se analiza el prefijo de la cadena de bits para ver que codigo binario coincide.
Al ser instantaneos siempre existe una unica coincidencia.
Cada vez que encuentro el codigo valido, se agrega el simbolo al mensaje codificado y se recorta la cantidad de bits utilizada
Esto se repite hasta llegar al final de la cadena, reconstruyendo el mensaje original.    
"""


def decodificacion_binaria(alfabeto_fuente, codificacion, mensaje_codificado):
    
    cadena = ""
    mensaje_decodificado = ""
    
    for i in mensaje_codificado:
        
        byte = bin(i)[2:].zfill(8)
        cadena += str(byte)
        
    resto = int(cadena[:8], 2)
    cadena = cadena[8:]
    
    if resto > 0:
        cadena = cadena[:-resto]
        
    dicionario_decodificacion = dict(zip(codificacion, alfabeto_fuente))
    
    while(len(cadena)>0):
            i=0 
            while(i < len(codificacion) and not cadena.startswith(codificacion[i])): # Buscar el código que coincide
                i+=1
            if i < len(codificacion):
                mensaje_decodificado+=alfabeto_fuente[i]
                cadena = cadena[len(codificacion[i]):] # Cortar la cadena
            else:
                print(f"ERROR DE DECODIFICACIÓN: Secuencia corrupta cerca de: '{cadena[:20]}...'")
                break # Rompe el 'while' principal

    return mensaje_decodificado

    """imprime un bytearray en formato binario 
    """
def imprimir_bytearray_en_binario(datos_bytes):
    
    cadena_binaria = ""
    
    for byte_val in datos_bytes:
       
        octeto = bin(byte_val)[2:].zfill(8)
        cadena_binaria += octeto
        
    return cadena_binaria

"""calcula cuantas veces esta conprimido el mensaje en base al original mensaje original / mensaje codificado  y me devuelve el n de N:1"""

def calculo_de_compresion(mensaje,mensaje_codificado):
    
    if len(mensaje_codificado)==0:
        return 0
    else:
        return len(mensaje.encode('utf-8'))/len(mensaje_codificado)

def codificacion_en_archivo(nombre_archivo,alfabeto,probabilidades,mensaje):
    
    codificacion=huffman_binario(probabilidades)
    mensaje_codificado=codificacion_binaria(alfabeto,codificacion,mensaje)
    
    try:
        # Usamos 'wb' (write binary) para escritura binaria
        with open(nombre_archivo, 'wb') as archivo:
            # Escribir el contenido del bytearray directamente
            archivo.write(mensaje_codificado)
        
        print(f"Bytearray almacenado con éxito en '{nombre_archivo}'.")
        return codificacion
    
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

def decodificar_desde_archivo(nombre_archivo,alfabeto,codificacion):
    
    try:
        with open(nombre_archivo, 'rb') as archivo:
            mensaje_codificado = archivo.read()
            # Convertir el objeto 'bytes' a 'bytearray'
            mensaje_codificado = bytearray(mensaje_codificado)
        
        print(f"Datos leídos con éxito de '{nombre_archivo}'.")
        
        return decodificacion_binaria(alfabeto,codificacion,mensaje_codificado)
    
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        
        return None
    
"""Primero recorro el mensaje, detectando las secuencias donde el mismo caracter aparece repetido
varias veces seguidas.
Para esto, cuento cuantas veces aparece el mismo caracter (hasta un maximo de 255
porque es el maximo valor que puede representar un byte).
Luego tomo el codigo ascii del caracter y agrego al resultado (que es un bytearray)
un byte con el codigo ascii y uno con el numero de repeticiones
Despues se avanza en el mensaje desde el primer caracter diferente.
Este proceso se repite hasta recorrer el mensaje por completo """
def RLC(mensaje):
    
    secuencia=bytearray()
    
    if len(mensaje)>0:
       i = 0
       N = len(mensaje)
       MAX = 255 
       
       while i < N:
           caracter_actual = mensaje[i]
           count = 1
           j = i + 1
           while j < N and mensaje[j] == caracter_actual and count < MAX:
               count += 1
               j += 1
           
           try:
               ascii_val = ord(caracter_actual) 
           except TypeError:
               
               raise ValueError("El mensaje contiene caracteres no válidos para la codificación ASCII.")
           
           secuencia.append(ascii_val) 
           secuencia.append(count)
           i = j 

    return secuencia
""" escribe el bytearray en formato 2R3L5C
agarra el priemer valor como la letra y el segundo como la cantidad 
"""

def RLC_to_string(secuencia_RLC):
    
    resultado = []
    
    for i in range(0, len(secuencia_RLC), 2):
        
        ascii_val = secuencia_RLC[i]
        caracter = chr(ascii_val)
        count = secuencia_RLC[i + 1]
        resultado.append(caracter + str(count))
        
    return "".join(resultado)

"""Primero comparo cada par de codigos binarios, recorriendo todos los pares posibles
Luego para cada uno de los codigos se recorre los bits  bits en paralelo y cuento en cuantas 
posiciones difieren, esto para calcular  la distancia de Hamming entre ambos códigos.
Luego se chequea con la min y en caso de la nueva ser menor se cambian 
Al finalizar se calcula la cantidad de errores detectables como la distancia -1
y la cantidad de errores corregibles como el piso de la ((distancia-1)/2)"""
def Hamming_errores_soluciones(codificacion_binaria):
   
    num_codigos = len(codificacion_binaria)
    if num_codigos < 2:
        return 0,0,0

    min = float('inf')
   
    for i in range(num_codigos):
        for j in range(i + 1, num_codigos):
            codigo_A = codificacion_binaria[i]
            codigo_B = codificacion_binaria[j]
            # Calcular la distancia entre el par
            distancia_actual =0
            for bit_a,bit_b in zip(codigo_A,codigo_B):
                if bit_a!=bit_b:
                    distancia_actual+=1
            
            # Actualizar la distancia mínima
            if distancia_actual < min:
                min = distancia_actual

    
    errores_detectables = min - 1
    
    
    errores_corregibles = math.floor((min - 1) / 2)
    
    
    if errores_detectables < 0: errores_detectables = 0
    if errores_corregibles < 0: errores_corregibles = 0

    return min,errores_detectables,errores_corregibles
""" Agarra un caracter lo escribe en un binario de 7 bits 
Cuenta la cantidad de unos que hay y si esta es par 
    se le pone un 0 al finanl y si es impar se le pone un 1 al final
"""

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

    """



Se recorre el mensaje de entrada, caracter por caracter.

Para cada caracter, se llama a la función paridad_caracter para obtener su byte de 8 bits
. Este byte se convierte en una fila de 8 bits (una lista de 1s y 0s) y se añade al final de la matriz.
Después, una vez que todos los caracteres del mensaje están en la matriz, se recorren las columnas (de la 0 a la 7) para calcular la paridad vertical.
Para cada columna, se cuentan cuántos bits "1" hay.
Si la cantidad total de "1" en esa columna es impar, se pone un "1" en la primera fila (la matriz[0]) de esa columna. Si es par, se queda en "0".
Al finalizar, la matriz está completa (con paridad horizontal en las filas , paridad vertical en las columnas y cruzada ).
Cada fila de bits se convierte en un string binario, luego en un número (byte), y se añade al bytearray mensaje_codificado_paridad.
El resultado que se devuelve es este bytearray es la  matriz de pariedad.
    
    """

def codificar_mensaje_con_paridad(mensaje):
    
    mensaje_codificado_paridad = bytearray()
    matriz=[[0]*8]
    for caracter in mensaje:
        # Usar la función de paridad para obtener el byte de 8 bits (entero 0-255)
        byte_con_paridad = paridad_caracter(caracter)
        cadena_binaria = bin(byte_con_paridad)[2:].zfill(8)
        fila_de_bits = [int(bit) for bit in cadena_binaria]
        matriz.append(fila_de_bits)
        
    for j in range(8):
        cant_unos=0
        for i in range(1,len(matriz)):
            if matriz[i][j]==1:
                cant_unos+=1
        if  cant_unos % 2 != 0:
            matriz[0][j]=1  
            
    for fila in matriz:
        
        bin_str = "".join(map(str, fila))

        byte_val = int(bin_str, 2)
        
        mensaje_codificado_paridad.append(byte_val)
    return mensaje_codificado_paridad

# NOTA: Asume que bits_a_caracter(bits_lista) está definida para convertir 7 bits a un carácter.
"""
Explicación del Código

Se recorre el mensaje_codificado_bytes de entrada, byte por byte. 
Cada byte se convierte en su representación de 8 bits (una lista de 1s y 0s) y esa lista se añade como una nueva fila a la matriz_recibida. 
Al finalizar este bucle, la matriz que se envió (incluyendo la fila de paridad vertical en la Fila 0) está completamente reconstruida.
Primero se hace la verivicacion del bit de pariedad cruzada ya que por convencion si este falla se descarta el mensaje, esto se hace porque no sabemos si fallo en alguno de los bit de pariedad o se dio alguna convimacion rara de errores
A continuacion por filas y por columnas de las pariedades y en caso de discrepancia se se guarda la columna o fila correspondiente en un vec_aux
Una vez terminado este proceso hay tres casos posibles:
Caso 1: Un solo error. Si hay exactamente una fila con error y exactamente una columna con error, el código ha localizado un único bit erróneo en la intersección de ambas. 
Procede a corregir el bit "volteándolo" (usando ^= 1) y avisa que el error fue corregido.
Caso 2: Sin error. Si ambas listas están vacías, el mensaje se recibe correctamente y no se hace nada.
Caso 3: Error múltiple. el error  no se puede localizar. 
El código avisa que descarta el mensaje y devuelve un string vacío.
Finalmente, si el mensaje fue aceptado (ya sea porque estaba bien o porque fue corregido), se recorre la matriz desde la fila uno reconstruyendo el mensaje agarrando los primeros 7 bits de cada fila 
"""
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
    """se pasa de una matriz con filas de este estilo "0001000" a un bytearray
    """
def mat_a_byte(matriz):
    mensaje=bytearray()
    for fila in matriz:
        
        byte_val = int(fila, 2)
        
        mensaje.append(byte_val)
    return mensaje
"""se pasa de una matriz con filas de este estilo [1,0,0,0,1,0,0] a un bytearray
"""
def matrix_to_bytearray(matriz_bits):

    byte_array_resultado = bytearray()
    
    for fila in matriz_bits:
        
        if len(fila) != 8:
            raise ValueError("Cada fila de la matriz debe contener exactamente 8 bits.")
            
        bin_str = "".join(map(str, fila))           
        byte_val = int(bin_str, 2)             
        byte_array_resultado.append(byte_val)
        
        
    return byte_array_resultado

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
    print("Info mutua original ",info_mutua_a_b(prob,mat))
    mat2=mat
    while i!=-1:
        mat_determinante = genera_mat_det(mat2,i,j)
        mat2=mat_compuesta(mat2,mat_determinante)
        imprimir_matriz_normal(mat2)
        
        print("Info mutua ",info_mutua_a_b(prob,mat2))
        
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



#-------------FALOPA----------------------------

def paridad_impar_caracter(carat): #impar
    """
    Toma un carácter (7 bits) y le añade un bit de paridad impar en 
    la 8ª posición (menos significativa después del shift).
    """
    ascii_val = ord(carat)
    cant_unos = ascii_val.bit_count()
    
    # Lógica para paridad impar:
    # Si la cantidad de '1' es par, agregamos un '1' para hacerla impar.
    # Si la cantidad de '1' es impar, agregamos un '0' para mantenerla impar.
    if cant_unos % 2 == 0:
        ascii_val = ascii_val << 1 | 1
    else:
        ascii_val = ascii_val << 1
    return ascii_val

def verificacion_impar(byte):
    """
    Verifica si un byte completo (8 bits) cumple con la regla 
    de paridad impar (total de unos debe ser impar).
    """
    total_de_unos = byte.bit_count()
    
    # La regla ahora es que el total de '1' DEBE ser impar
    if total_de_unos % 2 != 0:
         return True  # La regla (TOTAL IMPAR) se cumplió. Todo bien.
    else:
         return False # La regla (TOTAL IMPAR) se ROMPIÓ. Hubo error.
    
def codificar_mensaje_paridad_impar(mensaje):
    """
    Codifica un mensaje de string usando paridad impar LRC (filas) 
    y VRC (columnas).
    """
    mensaje_codificado_paridad = bytearray()
    matriz = [[0] * 8]
    for caracter in mensaje:
        # Usar la función de paridad (impar) para obtener el byte de 8 bits
        byte_con_paridad = paridad_impar_caracter(caracter) # <--- NOMBRE ACTUALIZADO
        cadena_binaria = bin(byte_con_paridad)[2:].zfill(8)
        fila_de_bits = [int(bit) for bit in cadena_binaria]
        matriz.append(fila_de_bits)
        
    # Calcular paridad vertical (VRC) para que sea impar
    for j in range(8):
        cant_unos = 0
        for i in range(1, len(matriz)):
            if matriz[i][j] == 1:
                cant_unos += 1
        
        # Si la cantidad de '1' en la columna es par, agregamos un '1' 
        # en la fila de paridad para hacer la columna impar.
        if cant_unos % 2 == 0:
            matriz[0][j] = 1   
            
    for fila in matriz:
        bin_str = "".join(map(str, fila))
        byte_val = int(bin_str, 2)
        mensaje_codificado_paridad.append(byte_val)
        
    return mensaje_codificado_paridad

def decodificar_corregir_paridad_impar(mensaje_codificado_bytes):
    """
    Decodifica un bytearray (recibido) que fue codificado con paridad impar
    cruzada. Intenta corregir un error de un solo bit.
    """
    mensaje_original = ""
    matriz_recibida = []
    for byte_val in mensaje_codificado_bytes:
        bits = [int(b) for b in bin(byte_val)[2:].zfill(8)]
        matriz_recibida.append(bits)
    
    # Se suman los bits de paridad vertical (columna 7) de las filas de datos (desde la fila 1)
    suma_col = sum(matriz_recibida[i][7] for i in range(len(matriz_recibida)))

    # Comprobación de paridad de paridades (ambas sumas deben ser IMPARES)
    # Si alguna es par, hay un error no corregible.
    if sum(matriz_recibida[0]) % 2 == 0 or (suma_col % 2 == 0):
        print("Error en paridad cruzada (debe ser impar). Se descarta el mensaje.")
    else:
        filas_con_error = []
        cols_con_error = [] 
        
        # Verificar paridad horizontal (LRC) en cada fila
        for i in range(len(matriz_recibida)):
            paridad_recibida = matriz_recibida[i][7]
            total_unos = sum(matriz_recibida[i][:7])
            
            # Cálculo de paridad impar
            lpc_calculado = 1 if total_unos % 2 == 0 else 0
            
            if lpc_calculado != paridad_recibida:
                filas_con_error.append(i)

        # Verificar paridad vertical (VPC) en cada columna
        for j in range(8):
            paridad_recibida = matriz_recibida[0][j]
            total_unos = sum(matriz_recibida[i][j] for i in range(1, len(matriz_recibida)))
            
            # Cálculo de paridad impar
            vpc_calculado = 1 if total_unos % 2 == 0 else 0
            
            if vpc_calculado != paridad_recibida:
                cols_con_error.append(j)

        
        if len(filas_con_error) == 1 and len(cols_con_error) == 1:
            fila_err = filas_con_error[0]
            col_err = cols_con_error[0]

            # Corregir el bit invirtiéndolo
            matriz_recibida[fila_err][col_err] ^= 1
            print("Error único detectado y corregido.")

        elif len(filas_con_error) == 0 and len(cols_con_error) == 0:
            pass # No se hace nada, el mensaje se acepta tal cual.
            
        else:
            print("Error múltiple o no localizable. Mensaje descartado.")
            return "" # Devolver cadena vacía
        
        # Decodificar el mensaje (corregido o no)
        for i in range(1, len(matriz_recibida)):
            # Tomar los 7 bits de datos
            bits_datos = matriz_recibida[i][:7]
            bin_str = "".join(map(str, bits_datos))
            mensaje_original += chr(int(bin_str, 2))
                
    return mensaje_original

def info_mutua_formula(priori,mat_canal):
    info=0
    prob_mutua=Prob_simultaneo(priori,mat_canal)
    prob_posti=Prob_posteriori(priori,mat_canal)
    for i in range(len(mat_canal)):
        for j in range(len(mat_canal[0])):
            if prob_mutua[i][j] > 0:
                info += prob_mutua[i][j] * math.log2(prob_posti[i][j] / (priori[i]))
    return info

def propiedad_simetrica(priori,canal):
    
    # Calcula los dos valores
    i_ab = info_mutua_a_b(priori, canal)
    i_ba = info_mutua_b_a(priori, canal)

    # Define una tolerancia (ej: 0.000000001)
    # abs_tol es la diferencia máxima absoluta permitida
    return math.isclose(i_ab, i_ba, abs_tol=1e-9)


def reducir_iterativamente_por_consola(mat,p):
    matriz_actual = mat

    while True:
        entrada = input("Ingrese c1 c2 (o -1 -1 para salir): ")
        c1, c2 = map(int, entrada.split())

        if c1 == -1 and c2 == -1:
            print("Fin de la reducción.")
            break

        nueva = reduce_mat_consola(matriz_actual, c1, c2)

        if nueva is None:
            print("No es reducción simple")
        else:
            matriz_actual = nueva
            print(info_mutua_a_b(p,matriz_actual))
            imprimir_matriz_normal(matriz_actual)

    return matriz_actual


def reduce_mat_consola(mat, c1, c2):
    """
    Intenta reducir mat usando c1 y c2.
    Si es reducción simple, devuelve la nueva matriz.
    Si no, devuelve None.
    """
    if is_lineal(mat, c1, c2):
        return mat_compuesta(mat, genera_mat_det(mat, c1, c2))
    else:
        return None



