from Util_REAL import *
m=[[0.6,0.4],[0.2,0.8]]
p=[0.5,0.5]
print(calcula_error(p,m))

m=[[0.6,0.3,0.1],[0.1,0.8,0.1],[0.3,0.3,0.4]]
p=[1/3,1/3,1/3]
print(calcula_error(p,m))
p=[1/8,3/8,4/8]
print(calcula_error(p,m))
p=[4/15,3/15,8/15]
print(calcula_error(p,m))