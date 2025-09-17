from Util import a11, longitud_media


c9=["==","<","<=",">",">=","<>"]
probs=[0.1,0.5,0.1,0.2,0.05,0.05]
c10=[")","[]","]]","([","[()]","([)]"]
c11=["/","*","-","*","++","+-"]
c12=[".,",";",",,",":","...",",:;"]
print(a11(c9,probs))
print(longitud_media(c9,probs))

print(a11(c10,probs))
print(longitud_media(c10,probs))

print(a11(c11,probs))
print(longitud_media(c11,probs))

print(a11(c12,probs))
print(longitud_media(c12,probs))