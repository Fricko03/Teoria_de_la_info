import Util

alfbeto=["x","y","z"]
prob=[0.5,0.1,0.4]

print(alfbeto)
print("Información:", [f"{x:.2f}" for x in Util.saca_INFO(prob)])
print(f"Entropia {Util.entropia(prob,Util.saca_INFO(prob)):.2f}")

alfbeto=["0","1"]
prob=[0.5,0.5]
print(alfbeto)
print("Información:", [f"{x:.2f}" for x in Util.saca_INFO(prob)])
print(f"Entropia {Util.entropia(prob,Util.saca_INFO(prob)):.2f}")

alfbeto=["A","B","C","D"]
prob=[0.1,0.3,0.4,0.2]
print(alfbeto)
print("Información:", [f"{x:.2f}" for x in Util.saca_INFO(prob)])
print(f"Entropia {Util.entropia(prob,Util.saca_INFO(prob)):.2f}")