import Util

mensaje="ABDAACAABACADAABDAADABDAAABDCDCDCDC"
alfabeto,probs=Util.Alfabeto_y_sus_probabilidades(mensaje)
ordena = list(zip(alfabeto, probs)) 
ordena.sort()                       
alfabeto, probs = zip(*ordena)       
print("Alfabeto:", [f"{x}" for x in alfabeto])
print("Probabil:", [f"{x:.2f}" for x in probs])
print(f"Entroopia: {Util.entropia_base_2(probs,Util.saca_INFO_base_2(probs))}")
