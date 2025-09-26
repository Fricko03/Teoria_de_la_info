import Parcial.Util as Util
c9=["AA","C","B","AB","ACB"]#[")","[]","]]","([","[()]","([)]"]
alfabeto=Util.obtener_alfabeto_codigo(c9)
print(alfabeto )
longitud_pal=Util.obtener_longitudes_cod(c9)
print(longitud_pal)
print(Util.sum_ine_kraft(c9))