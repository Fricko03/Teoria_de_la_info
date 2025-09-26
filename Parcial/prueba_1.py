#from numpy import sort
from Util import Alfabeto_y_sus_probabilidades


mensaje="bvbvbvbvbvnvhbvbvbvbvbvnh"

#alfa,prob=Alfabeto_y_sus_probabilidades(mensaje)

# ordenacion
alfa,prob=Alfabeto_y_sus_probabilidades(mensaje)
print(alfa)
print(prob)
ordena = sorted(zip(alfa, prob))
alfa, prob = map(list, zip(*ordena))

print(alfa)
print(prob)
