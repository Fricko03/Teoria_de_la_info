import Util
mensaje1="CAAACCAABAACBBCABACCAAABCBBACC"
mensaje2="BBAAACCAAABCCCAACCCBBACCAABBAA"
tol=0.1
mat1,alfabeto1=Util.alfabeto_mat_con_mem(mensaje1)
mat2,alfabeto2=Util.alfabeto_mat_con_mem(mensaje2)

# print(Util.is_mem_nula(mat1,tol)
# )
# print(Util.is_mem_nula(mat2,tol))

Util.Estacionario(mat2,0.01)