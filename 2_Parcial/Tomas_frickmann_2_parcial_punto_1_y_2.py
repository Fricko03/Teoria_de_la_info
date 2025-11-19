
# ---------------------------------------SEGUNDO PARCIAL----------------------------------------------------
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
def primerteoremaShanon(probabilidad,codigoextendido,N,entropia,extension_real):
    
    alfabeto_vacio=[""]*len(probabilidad)
    _,probexte=extendida_bien(alfabeto_vacio,probabilidad,N)
    longitud=longitud_media(codigoextendido,probexte)
    
    
    print("Longitud",longitud)
    print("Entropia",entropia)
    print(entropia,"<=",longitud/extension_real,"<=",(entropia+1/extension_real))
    
    return entropia<=longitud/extension_real<=(entropia+1/extension_real)

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
    # iteracion =1
    if len(items)==1:
        
        return ["0"]
    
    while len(items)>1:
        
        items = sorted(items, key=lambda x: x[0],reverse=True)
        # print("Iteracion= ",iteracion)
        # print("Items ordenados",items)
        menor_1=items.pop()
        menor_2=items.pop()
        # print("se agrega 0 a ",menor_1[1])
        # print("se agrega 1 a ",menor_2[1])
        
        for i in menor_1[1]:
            codigos[i] = '0' + codigos[i]
        
        for i in menor_2[1]:
            codigos[i] = '1' + codigos[i]
            
        items.append([menor_2[0]+menor_1[0],menor_1[1]+menor_2[1]])
        # nuevo=[menor_2[0]+menor_1[0],menor_1[1]+menor_2[1]]
        # print("nuevo nodo:", nuevo)
        # print("items ahora:", items)
        # iteracion+=1
    # print("\ncodigos finales:", codigos)
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
        print(f"\ntotal probabilidades: {prob_tot}     con el conjunto: {items}")
        while (i<=n-1 and acum<prob_tot/2):
            acum+=items[i][0]
            i+=1
            
        for j in range(i-1,n):
            resto+=items[j][0]

        if acum>resto:
            i=i-1
            
        cod_1= items[0:i]
        cod_0=items[i:]
        print(f"conjunto 1: ", cod_1)
        print(f"conjunto 2: ", cod_0)
        for j in cod_0:
            cods[j[1]]=cods[j[1]]+'0'
           
        for j in cod_1:
            cods[j[1]]=cods[j[1]]+'1'
        print(f"codigos parciales: ", cods)
        _shanon_rec_bin(cod_0,cods)
        _shanon_rec_bin(cod_1,cods)
    
def shanon_binario(probs):
    if len(probs)==1:
        return ["0"]
    
    items = [[p, i] for i, p in enumerate(probs)]
    codigos = [''] * len(probs)
    items = sorted(items, key=lambda x: x[0],reverse=True)
    _shanon_rec_bin(items,codigos)
    print("Items iniciales ordenados:", items)
    
    print("Códigos finales:", codigos)
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
        # print(octeto)
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


mensaje="DCDAACDAADDDACCCCABD"
print("--------------ICISO A----------")
alf,prob=Alfabeto_y_sus_probabilidades(mensaje)
print("El alfabeto es: ",alf)
print("La probabilidad  es: ",prob)
entropia_original=entropia_base_2(prob,saca_INFO_base_2(prob))
print(f"La H2(S) es :{entropia_original:.2}")

print("--------------ICISO B----------")
cod_huf=huffman_binario(prob)
print("El codigo binario optimo encontrado por Huffman es: ",cod_huf)

print("--------------ICISO C----------")
mensaje_cod=codificacion_binaria(alf,cod_huf,mensaje)
mensaje_cod=imprimir_bytearray_en_binario(mensaje_cod)
print("El mensaje original es: ",mensaje)
mensaje_cod=mensaje_cod[8:]
print("El mensaje codificao es:",mensaje_cod)

tasa_N=calculo_de_compresion(mensaje,mensaje_cod)
print("La tas de compresion es ",tasa_N,"/1")


print("--------------ICISO D----------")
alf_exte_3,prob_exte_3=extendida_bien(alf,prob,3)
cod_huf_exte3=huffman_binario(prob_exte_3)
print("El codigo binario optimo encontrado por Huffman es: ",cod_huf_exte3)

print("--------------ICISO E----------")
l_media=longitud_media(cod_huf,prob)
rendimiento,redundancia=calculo_redundancia_rendimiento(prob,cod_huf)
print("Logitud media del cod original: ",l_media)
print("Rendimiento de cod original: ",rendimiento)
print("Redundancia del cod original:", redundancia)

l_media_3=longitud_media(cod_huf_exte3,prob_exte_3)
rendimiento_3,redundancia_3=calculo_redundancia_rendimiento(prob_exte_3,cod_huf_exte3)
print("Logitud media del cod extendida: ",l_media_3)
print("Rendimiento de cod extendida: ",rendimiento_3)
print("Redundancia del cod extendida:", redundancia_3)


print("--------------ICISO F----------")



if primerteoremaShanon(prob,cod_huf,1,entropia_original,1):
    print("EEl codigo original cunple el teoriema de Shannon")
else:
    print("El codigo original no cumple el teorema de shannon")
    
if primerteoremaShanon(prob_exte_3,cod_huf_exte3,1,entropia_original,3):
    print("EEl codigo extendido cunple el teoriema de Shannon")
else:
    print("El codigo extendido no cumple el teorema de shannon")
mensaje_cod_2=RLC(mensaje)
mensaje_cod_2=RLC_to_string(mensaje_cod_2)
print("El mensaje original es: ",mensaje)
mensaje_cod_2=mensaje_cod_2[8:]

print("El mensaje codificao es:",mensaje_cod_2)
tasa_N_2=calculo_de_compresion(mensaje,mensaje_cod_2)
print("La tas de compresion es ",tasa_N_2,"/1")
