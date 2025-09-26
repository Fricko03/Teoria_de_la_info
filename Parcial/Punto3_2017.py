from Util import *


M=[
    [0,1/4,1/5,0,1/6],
    [1/3,0,1/5,0,1/6],
    [1/2,1/2,1/5,1/2,1/6],
    [1/6,0,1/5,1/2,1/6],
    [0,1/4,1/5,0,1/3]    
] 

ve_estac=Estacionario(M,0.001)
print(ve_estac)


etro=Entropia_con_mem(M,ve_estac)
print(etro)