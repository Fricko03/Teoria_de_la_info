from Util_REAL import *
# ## punto2

# # probs=[0.5,0.2,0.3]
# # alfa=["s1","s2","s3"]
# # cod=["1","00","01"]

# # print(primerteoremaShanon(probs,cod,1))
# # cod,_=extendida_bien(cod,probs,2)

# # print(primerteoremaShanon(probs,cod,2))

# #punto 3

# # probs=[0.3,0.1,0.4,0.2]
# # alfa=["s1","s2","s3","s4"]
# # cod=["0","10","110","1110"]
# # cod,_=extendida_bien(cod,probs,2)

# # print(primerteoremaShanon(probs,cod,2))

# #punto 4

# # probs=[0.9,0.1]
# # alfa=["s1","s2"]
# # cod=["0","1"]

# # cod,_=extendida_bien(cod,probs,5)

# # print(primerteoremaShanon(probs,cod,5))

# # ##punto 5 
# # probs=[0.385,0.179,0.154,0.154,0.128]
# # cod=["0","111","110","101","100"]
# # cod2=["00","01","10","110","111"]

# # print(calculo_redundancia_rendimiento(probs,cod))

# # print(calculo_redundancia_rendimiento(probs,cod2))


# # punto8
# # probs=[0.3,0.1,0.4,0.2]
# # cod=["10","1110","0","110"]
# # print(calculo_redundancia_rendimiento(probs,cod))

# #puhto 10

# # mensaje="ABSDABSBDSBAAABBBSBSBABADBSBABSBDBSSSAAABB"
# # alfa,prob=Alfabeto_y_sus_probabilidades(mensaje)
# # print(alfa,prob)
# # print(huffman_binario(prob))
# # #punto 11
# # mensaje="AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO"
# # alfa,prob=Alfabeto_y_sus_probabilidades(mensaje)
# # print(alfa,prob)
# # print(shanon_binario(prob))

# ###punto 12 
# # mensaje="05987463258784784512536669895745123656253698989656452121702300223659"
# # alfa,prob=Alfabeto_y_sus_probabilidades(mensaje)
# # huf=(huffman_binario(prob))
# # shano=(shanon_binario(prob))
# # print(calculo_redundancia_rendimiento(prob,huf))
# # print(longitud_media(huf,prob))
# # print(calculo_redundancia_rendimiento(prob,shano))
# # print(longitud_media(shano,prob))
# ##punto 13
# # prob=[0.2,0.2,0.3,0.3]
# # print(huffman_binario(prob))
# #punto14

# # probs=[0.4,0.25,0.25,0.1]
# # print(shanon_binario(probs))
# ##Punto 16
# # s2 = ["A", "B", "C", "D", "E"]
# # prob = [0.385, 0.154, 0.128, 0.154, 0.179] 
# # print(entropia_base_2(prob,saca_INFO_base_2(prob)))
# # print(s2)
# # print(huffman_binario(prob))
# # print(shanon_binario(prob))

# # #punto 17 
# # # a) F = {s1 } con PF = {1}
# # F_a = ["s1"]
# # PF_a = [1.0]

# # # b) F = {s1, s2} con PF = {0.5, 0.5}
# # F_b = ["s1", "s2"]
# # PF_b = [0.5, 0.5]

# # # c) F = {s1, s2, s3} con PF = {0.6, 0.3, 0.1}
# # F_c = ["s1", "s2", "s3"]
# # PF_c = [0.6, 0.3, 0.1]

# # # d) F = {s1, s2, s3, s4, s5} con PF = {0.6, 0.1, 0.1, 0.1, 0.1}
# # F_d = ["s1", "s2", "s3", "s4", "s5"]
# # PF_d = [0.6, 0.1, 0.1, 0.1, 0.1]

# # # e) F = { s1, s2, s3, s4, s5} con PF = {0.2, 0.1, 0.4, 0.1, 0.1}
# # # (Se asumió 0.1 como la última probabilidad para completar 5 valores y sumar 1.0)
# # F_e = ["s1", "s2", "s3", "s4", "s5"]
# # PF_e = [0.2, 0.1, 0.4, 0.1, 0.1]
# # print(huffman_binario(PF_e))

# ##print 18
# a=["s1","s2","s3"]
# prob=[0.5,0.2,0.3]
# print(huffman_binario(prob))
# _,prob=extendida_bien(a,prob,2)
# print(huffman_binario(prob))

# prob=[0.5,0.2,0.3]
# print(longitud_media(huffman_binario(prob),(prob)))
# _,prob=extendida_bien(a,prob,2)

# print(longitud_media(huffman_binario(prob),(prob)))

# #Punto 16
# s2 = ["A", "B", "C", "D", "E"]
# prob = [0.385, 0.154, 0.128, 0.154, 0.179] 

# huf=(huffman_binario(prob))
# sha=(shanon_binario(prob))
# print(calculo_redundancia_rendimiento(prob,huf))

# print(calculo_redundancia_rendimiento(prob,sha))


# ##punto 25 

# c1=["01" , "10", "11", "00"]
# c2=["000", "100", "101","111"]
# c3=["0000",
#  "0011",
#  "1010",
#  "0101"]

# print(Hamming_errores_soluciones(c1))

# print(Hamming_errores_soluciones(c2))

# print(Hamming_errores_soluciones(c3))
##punto 31

c1=["0100001","0100010"]