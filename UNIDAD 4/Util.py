#Importacion de librerias

import random
import copy
import math



#FUENTE SIN MEMORIA

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
    return alfabeto,probabilidades

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


def obtener_alfabeto_codigo(lista_pal_cod):
    alfa_cod=[]
    for i in lista_pal_cod:
        for j in i:
            if j not in alfa_cod:
                alfa_cod.append(j)
    return alfa_cod

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
#ver si debo extender el codigo de codificacion antes de hacerlo 
def primerteoremaShanon(probabilidad,codigoextendido,N):
    alfabeto_vacio=[""]*len(probabilidad)
    _,probexte=extendida_bien(alfabeto_vacio,probabilidad,N)
    longitud=longitud_media(codigoextendido,probexte)
    entropia=entropia_base_r(codigoextendido,probabilidad)
    print("Longitud",longitud)
    print("Entropia",entropia)
    return entropia<=longitud/N<=(entropia+1/N)


def calculo_redundancia_rendimiento(probabilidades,codificacion):
    entropia=entropia_base_r(codificacion,probabilidades)
    logitud=longitud_media(codificacion,probabilidades)
    return entropia/logitud,(1-entropia/logitud)


def huffman_binario(probs):
    items = [[p, [i]] for i, p in enumerate(probs)]
    codigos = [''] * len(probs)
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

# 15. Implementar funciones en Python que reciban como parámetros: una cadena de
# caracteres que contenga un alfabeto fuente y una lista de cadenas de caracteres que
# almacena una codificación en el alfabeto binario, y resuelvan lo siguiente:
# a. Dada una cadena de caracteres con un mensaje escrito en el alfabeto fuente,
# devolver una secuencia de bytes (bytearray) que contenga el mensaje codificado.
# b. Dada una secuencia de bytes, decodificar y retornar el mensaje original.
# Sugerencia: manipular el mensaje codificado como una cadena de caracteres de unos y
# ceros, tanto para codificar como para decodificar, y realizar las conversiones entre binarios
# y enteros con las funciones de casteo correspondientes.

    
    
def codificacion_binaria(alfabeto_fuente,codificacion,mensaje):
    cadena=bytearray()
    cadena_str="" #estos tres primero que pongo son para ver cuanto residuo tengo
    dicionario_codificacion=dict(zip(alfabeto_fuente,codificacion))
    for i in mensaje:
        cadena_str+=dicionario_codificacion[i]
    resto=(8-(len(cadena_str)+3)%8)%8
    if resto!=0:
        cadena_str+="0"*(resto)
    resto=bin(resto)[2:].zfill(3)
    cadena_str=resto+cadena_str
    for i in range(0,len(cadena_str),8):
        cadena.append(int(cadena_str[i:i+8],2))
    return cadena   
    
def decodificacion_binaria(alfabeto_fuente,codificacion,mensaje_codificado):
    cadena=""
    mensaje_decodificado=""
    
    
    for i in mensaje_codificado:
        byte=bin(i)[2:].zfill(8)
    
        cadena+=str(byte)
    resto = int(cadena[:3], 2)
    cadena=cadena[3:]
    if resto>0:
        cadena=cadena[:-resto]
    while(len(cadena)>0):
        i=0 
        while(not cadena.startswith(codificacion[i])):
            i+=1
        mensaje_decodificado+=alfabeto_fuente[i]
        cadena = cadena[len(codificacion[i]):]

    return mensaje_decodificado        
        

def imprimir_bytearray_en_binario(datos_bytes):
    
    cadena_binaria = ""
    for byte_val in datos_bytes:
       
        octeto = bin(byte_val)[2:].zfill(8)
        cadena_binaria += octeto
    return cadena_binaria

## me da el n de N:1
def calculo_de_compresion(mensaje,mensaje_codificado):
    
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



import math



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


def paridad_caracter(carat):#par
    
    ascii_val = ord(carat)
    cant_unos = ascii_val.bit_count()
    if cant_unos%2==0:
        ascii_val=ascii_val<<1
    else:
        ascii_val=ascii_val<<1|1
    return ascii_val

def verificacion(byte):
    total_de_unos = byte.bit_count()
    if total_de_unos % 2 == 0:
         return True  # La regla (TOTAL PAR) se cumplió. Todo bien.
    else:
        return False # La regla (TOTAL PAR) se ROMPIÓ. Hubo error.
    
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

def decodificar_y_corregir_paridad(mensaje_codificado_bytes):
   
    

   
    matriz_recibida = []
    for byte_val in mensaje_codificado_bytes:
       
        bits = [int(b) for b in bin(byte_val)[2:].zfill(8)]
        matriz_recibida.append(bits)


    
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

    
    mensaje_original = ""
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