import ENTRO_INFO
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

def diferencia(vp,va):
    aux=[]
    for i in range(len(vp)):
        aux.append(abs(vp[i]-va[i]))
    return max(aux)

def Entropia_con_mem(mat_transicion,vec_esta):
    suma=[]
    
    num_filas = len(mat_transicion)
    num_columnas = len(mat_transicion[0])
    for i in range(num_columnas):
        columna = [fila[i] for fila in mat_transicion]
        suma.append(ENTRO_INFO.entropia(columna,ENTRO_INFO.sacaprob(columna))*vec_esta[i])    
    
    return sum(suma)

mat=[[1/3, 0 , 1 , 1/2,0],
     [1/3, 0 , 0 , 0  ,0],
     [0  , 1 , 0 , 0  ,0],
     [1/3, 0 , 0 , 0,1/2],
     [0, 0 , 0 , 1/2,1/2]
    ]
vec=Estacionario(mat,0.0001)
for i in vec:
    print(f"{i:.2f}")
print(f"Vector estacionario{vec}")
print(f"{3/9}")
print(f"{1/9}")
print(f"{1/9}")
print(f"{2/9}")
print(f"{2/9}")
print(f"{Entropia_con_mem(mat,vec):.2f}")