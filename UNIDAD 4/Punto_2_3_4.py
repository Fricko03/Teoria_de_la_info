from Util import *
# prob=[0.3,0.1,0.4,0.2]
# cod=["BA","CAB","A","CBA"]
# cod_exte1,_=calc_exte(cod,prob,2)
# print(primerteoremaShanon(prob,cod_exte1,2))

prob=[0.5,0.2,0.3]
cod1=["11","010","00"]
print(primerteoremaShanon(prob,cod1,1))

cod2=["10","001","110","010","0000","0001","111","0110","0111"]

print(primerteoremaShanon(prob,cod2,2))

prob=[0.8,0.2]
cod=["0","1"]
cod_exte1,_=calc_exte(cod,prob,3)
print(primerteoremaShanon(prob,cod_exte1,3))