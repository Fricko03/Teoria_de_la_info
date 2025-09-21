from Util import entropia_base_r, longitud_media


c9=["==","<","<=",">",">=","<>"]
probs=[0.1,0.5,0.1,0.2,0.05,0.05]
c10=[")","[]","]]","([","[()]","([)]"]
c11=["/","*","-","*","++","+-"]
c12=[".,",";",",,",":","...",",:;"]
print(entropia_base_r(c9,probs))
print(longitud_media(c9,probs))

print(entropia_base_r(c10,probs))
print(longitud_media(c10,probs))

print(entropia_base_r(c11,probs))
print(longitud_media(c11,probs))

print(entropia_base_r(c12,probs))
print(longitud_media(c12,probs))