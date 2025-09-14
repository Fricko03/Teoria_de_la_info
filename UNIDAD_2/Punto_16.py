import Util
mensaje1="CAAACCAABAACBBCABACCAAABCBBACC"
mensaje2="BBAAACCAAABCCCAACCCBBACCAABBAA"
tol=0.1
mat1,alfabeto1=Util.alfabeto_mat_con_mem(mensaje1)
mat2,alfabeto2=Util.alfabeto_mat_con_mem(mensaje2)

Util.clasificacion_fuente(mat1,tol)

Util.clasificacion_fuente(mat2,tol)