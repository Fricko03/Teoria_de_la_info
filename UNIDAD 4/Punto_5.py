from Util import *

alfabeto=["0","1"]
prob=[0.7,0.3]

alfext,probexte=calc_exte(alfabeto,prob,2)
print(alfext)
print(probexte)
ordena = sorted(zip(alfext, probexte))
alfext, probexte = map(list, zip(*ordena))
print(shanon_binario(probexte))