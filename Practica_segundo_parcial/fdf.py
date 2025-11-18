def ShannonFanoR(items, codigo):
    N = len(items) 
    if N > 1:
        total=0
        for i in range(len(items)):
            total += items[i][0]
        
        # print(f"\ntotal probabilidades: {total}     con el conjunto: {items}")

        i=0
        acum=0
        #acumulo probabilidad hasta superar la mitad del total
        while( acum <= total/2.0):
            acum += items[i][0]
            i+=1

        #calculo el acumulado de probabilidades considerando el limite
        resto=0
        for j in range(i-1,len(items)):
            resto += items[j][0]
        #me fijo en que division dejo el limite, poniendolo en el que menor acumulado tenga
        if acum > resto:
            conj1 = items[:i-1]
            conj2 = items[i-1:]
        else:
            conj1 = items[:i] 
            conj2 = items[i:] 

        # print(f"conjunto 1: ", conj1)
        # print(f"conjunto 2: ", conj2)
        

        for i in range(len(conj1)):
            codigo[conj1[i][1]] = codigo[conj1[i][1]] + "1"
        
        for j in range(len(conj2)):
            codigo[conj2[j][1]] = codigo[conj2[j][1]] + "0" 

        # print(f"codigos parciales: ", codigo)

        ShannonFanoR(conj1,codigo)
        ShannonFanoR(conj2,codigo)

def ShannonFano(probabilidades):
    items = [[p,i] for i,p in enumerate(probabilidades)]
    items = sorted(items, key=lambda x: x[0], reverse=True)
    # print("Items iniciales ordenados:", items)
    codigo = [""]*len(probabilidades)
    ShannonFanoR(items,codigo)
    # print("Códigos finales:", codigo)
    return codigo