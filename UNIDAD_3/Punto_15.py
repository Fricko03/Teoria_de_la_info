from Parcial.Util import is_compacto


c9=["==","<","<=",">",">=","<>"]
probs=[0.1,0.5,0.1,0.2,0.05,0.05]
c10=[")","[]","]]","([","[()]","([)]"]
c11=["/","*","-","*","++","+-"]
c12=[".,",";",",,",":","...",",:;"]

print(is_compacto(c9,probs))

print(is_compacto(c10,probs))

print(is_compacto(c11,probs))

print(is_compacto(c12,probs))