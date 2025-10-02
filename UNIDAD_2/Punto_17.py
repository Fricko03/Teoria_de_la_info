import Util
M=[[1/2,0,0,1/2],
   [1/2,0,0,0],
   [0,1/2,0,0],
   [0,1/2,1,1/2]]
v=Util.Estacionario(M,0.001)
print(v)