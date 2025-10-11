from Util import *


prob=[0.5,0.2,0.3]
cod1=["11","010","00"]

print(calculo_redundancia_rendimiento(prob,cod1))

cod2=["10","001","110","010","0000","0001","111","0110","0111"]
_,probexte=calc_exte(cod2,prob,2)
print(calculo_redundancia_rendimiento(probexte,cod2))
print()
probs=[0.2,0.15,0.1,0.3,0.25]
c1=["01","111","110","101","100"]
c2=["00","01","10","110","111"]
c3=["0110","010","0111","1","00"]
c4=["11","001","000","10","01"]

vec=[c1,c2,c3,c4]
for i in vec:
    print(calculo_redundancia_rendimiento(probs,i))