import Util

alfbeto=["x","y","z"]
prob=[0.5,0.1,0.4]
n=2
alfabeto_exte,probs_exte=Util.extendida_bien(alfbeto,prob,n)
     
print("Alfabeto:", [f"{x}" for x in alfabeto_exte])
print("Probabil:", [f"{x:.2f}" for x in probs_exte])

print(f"Entroopia normal: {Util.entropia_base_2(prob,Util.saca_INFO_base_2(prob))}")
print(f"Entropia n*h(s) : {Util.entropia_base_2(prob,Util.saca_INFO_base_2(prob))*n}")

print(f"Entropia 2 : {Util.entropia_base_2(probs_exte,Util.saca_INFO_base_2(probs_exte)):.2f}")

alfabeto_exte,probs_exte=Util.calc_exte(alfbeto,prob,3)
print("Alfabeto:", [f"{x}" for x in alfabeto_exte])
print("Probabil:", [f"{x:.2f}" for x in probs_exte])
print(f"Entropia 3 : {Util.entropia_base_2(probs_exte,Util.saca_INFO_base_2(probs_exte)):.2f}")

alfbeto=["0","1"]
prob=[0.5,0.5]
alfabeto_exte,probs_exte=Util.extendida_bien(alfbeto,prob,n)
     
print("Alfabeto:", [f"{x}" for x in alfabeto_exte])
print("Probabil:", [f"{x:.2f}" for x in probs_exte])

print(f"Entroopia normal: {Util.entropia_base_2(prob,Util.saca_INFO_base_2(prob))}")
print(f"Entropia n*h(s) : {Util.entropia_base_2(prob,Util.saca_INFO_base_2(prob))*n}")

print(f"Entropia 2 : {Util.entropia_base_2(probs_exte,Util.saca_INFO_base_2(probs_exte)):.2f}")

alfabeto_exte,probs_exte=Util.calc_exte(alfbeto,prob,3)
print("Alfabeto:", [f"{x}" for x in alfabeto_exte])
print("Probabil:", [f"{x:.2f}" for x in probs_exte])
print(f"Entropia 3 : {Util.entropia_base_2(probs_exte,Util.saca_INFO_base_2(probs_exte)):.2f}")

alfbeto=["A","B","C","D"]
prob=[0.1,0.3,0.4,0.2]

alfabeto_exte,probs_exte=Util.extendida_bien(alfbeto,prob,n)
     
print("Alfabeto:", [f"{x}" for x in alfabeto_exte])
print("Probabil:", [f"{x:.2f}" for x in probs_exte])

print(f"Entroopia normal: {Util.entropia_base_2(prob,Util.saca_INFO_base_2(prob))}")
print(f"Entropia n*h(s) : {Util.entropia_base_2(prob,Util.saca_INFO_base_2(prob))*n}")

print(f"Entropia 2 : {Util.entropia_base_2(probs_exte,Util.saca_INFO_base_2(probs_exte)):.2f}")

alfabeto_exte,probs_exte=Util.calc_exte(alfbeto,prob,3)
print("Alfabeto:", [f"{x}" for x in alfabeto_exte])
print("Probabil:", [f"{x:.2f}" for x in probs_exte])
print(f"Entropia 3 : {Util.entropia_base_2(probs_exte,Util.saca_INFO_base_2(probs_exte)):.2f}")