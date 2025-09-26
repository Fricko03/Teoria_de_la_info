from  Parcial.Util import propiedades 

if __name__ == "__main__":
    c1=["011","000","010","101","001","100"]
    c2=["110","100","101","001","110","010"]
    c3=["10","1100","0101","1011","0","110"]
    c4=["1101","10","1111","1100","1110","0"]
    c5=["011","0111","01","0","011111","01111"]
    c6=["1110","0","110","1101","1011","10"]
    c7=["010","101","000","111"]
    c8=["110","001","11","00"]

    # propiedades(c1)
    # propiedades(c2)
    # propiedades(c3)
    # propiedades(c4)
    # propiedades(c5)
    # propiedades(c6)
    # propiedades(c7)
    # propiedades(c8)
    # print("--------Punto 8-----------")
    # c9=["==","<","<=",">",">=","<>"]
    # c10=[")","[]","]]","([","[()]","([)]"]
    # c11=["/","*","-","*","++","+-"]
    # c12=[".,",";",",,",":","...",",:;"]

    # propiedades(c9)
    # propiedades(c10)
    # propiedades(c11)
    # propiedades(c12)
    # Conjuntos de prueba: fuentes complejas
    fuentes = {
    "F1_letras_prefijo": ['a', 'bc', 'bcd'],      # ✅ Instantánea, UD
        "F2_letras_no_prefijo": ['a', 'ab', 'abc'],   # ❌ Instantánea, ✅ UD
        "F3_no_UD": ['a', 'ab', 'ba'],               # ❌ No UD
        "F4_palabras_cortas": ['x', 'y', 'z'],       # ✅ Bloque, UD, instantánea
        "F5_mixta_letras": ['m', 'mn', 'mno', 'mnop'], # ✅ Instantánea, UD
        "F6_numeros_letras": ['1', '12', '123', '1234'], # ✅ Instantánea, UD
        "F7_confusa": ['p', 'pq', 'q'],              # ❌ No UD
        "F8_variable_longitud": ['g', 'gh', 'ghi', 'ghij'], # ✅ Instantánea, UD
        "F9_singular": ['r', 's', 'tuv'],            # ✅ UD, instantánea
        "F10_ambigua": ['a', 'ab', 'b', 'ba'],       # ❌ No UD "F10_muy_larga": ['1', '10', '110', '1110', '11110'], # ✅ Prefijo libre, UD
    }

    # Ejemplo de uso
    for nombre, fuente in fuentes.items():
        print(f"{nombre}:") 
        propiedades(fuente)