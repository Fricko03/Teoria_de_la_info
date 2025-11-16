from Util_REAL import *
prob1=[1/3,1/3,1/3]

c1=[[1, 0, 0,],[
 0 ,0 ,1],
 [0, 1, 0]]

c2=[[ 1/2, 1/2, 0],
 [0 ,1/4 ,3/4]]

if (not is_not_ruidosa(c1)):
    print(entropia_ruido(prob1,c1))
else:
    print("sin ruido")
    
print(entropia_perdida(prob1,c1))
prob2=[0.5,0.5]
if (not is_not_ruidosa(c2)):
    print(entropia_ruido(prob2,c2))
else:
    print("sin ruido")
    
print(entropia_perdida(prob2,c2))