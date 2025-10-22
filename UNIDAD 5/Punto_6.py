from Util import *
probs_prio=[0.3,0.3,0.4]
probcal=[[0.4,0.4,0.2],
         [0.3,0.2,0.5],
         [0.3,0.4,0.3]]
# print(Prob_de_b(probs_prio,probcal))
# mat=Prob_posteriori(probs_prio,probcal)
# print(mat)
# for i in mat:
#     print(i,end="\n")
print(Prob_simultaneo(probs_prio,probcal))
