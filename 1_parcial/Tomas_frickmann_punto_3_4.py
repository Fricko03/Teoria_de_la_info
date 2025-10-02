import math

from cycler import K
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
    print(C1)
    print(s1)
    K=1
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
        print("Lista de conjuntos",lista_de_S)
        print(f"iteracion {K} conjunto obtenido: ")
        print(s_aux)
        K=K+1
        
    
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


    
    
def sum_ine_kraft(lista_pal_cod):
    r=len(obtener_alfabeto_codigo(lista_pal_cod))
    longitudes=obtener_longitudes_cod(lista_pal_cod)
    suma= [r**(-i) for i in longitudes]
    return sum(suma)
##ejercicio 4 
codigo=[";.",",",".:",":",",;"]
probabilidades=[0.15,0.25,0.05,0.45,0.10]

##---------------punto a ---------
alf_codigo=obtener_alfabeto_codigo(codigo)
print(f"El alfabeto con digo es: {alf_codigo}")


##---------------punto b ---------

entropia=entropia_base_r(codigo,probabilidades)
longitud=longitud_media(codigo,probabilidades)

print(f"El codigo tiene una entropia de {entropia:.2f} y un alogitud media de {longitud:.2f}")

##---------------punto c ---------
suma=sum_ine_kraft(codigo)
if (suma<=1):
    print(f"Con las logitudes dadas el codigo cumple la inecuación de Kraft-McMillan, valor={suma:.2f}")
else:
    print(f"Con las logitudes dadas el codigo no cumple la inecuación de Kraft-McMillan, valor={suma:.2f}")

##---------------punto d ---------

propiedades(codigo)

##---------------punto e ---------
if (is_compacto(codigo,probabilidades)):
    print("El codigo dado es conpacto")
else:
    print("El codigo dado no es compacto")
    
    
print()
print()
print()
print("ACA COMIENZA EL EJERCICIO 4")
print()
print()
print()

codigo=["(]","]","[)",")","(["]
probabilidades=[0.15,0.25,0.05,0.45,0.10]

##---------------punto a ---------
alf_codigo=obtener_alfabeto_codigo(codigo)
print(f"El alfabeto con digo es: {alf_codigo}")


##---------------punto b ---------

entropia=entropia_base_r(codigo,probabilidades)
longitud=longitud_media(codigo,probabilidades)

print(f"El codigo tiene una entropia de {entropia:.2f} y un alogitud media de {longitud:.2f}")

##---------------punto c ---------
suma=sum_ine_kraft(codigo)
if (suma<=1):
    print(f"Con las logitudes dadas el codigo cumple la inecuación de Kraft-McMillan, valor={suma:.2f}")
else:
    print(f"Con las logitudes dadas el codigo no cumple la inecuación de Kraft-McMillan, valor={suma:.2f}")

##---------------punto d ---------

propiedades(codigo)

##---------------punto e ---------
if (is_compacto(codigo,probabilidades)):
    print("El codigo dado es conpacto")
else:
    print("El codigo dado no es compacto")