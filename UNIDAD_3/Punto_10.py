from Parcial.Util import propiedades, sum_ine_kraft

if __name__ == "__main__":
    c1 = ["011", "000", "010", "101", "001", "100"]
    c2 = ["110", "100", "101", "001", "110", "010"]
    c3 = ["10", "1100", "0101", "1011", "0", "110"]
    c4 = ["1101", "10", "1111", "1100", "1110", "0"]
    c5 = ["011", "0111", "01", "0", "011111", "01111"]
    c6 = ["1110", "0", "110", "1101", "1011", "10"]
   

    print(sum_ine_kraft(c1))
    print(sum_ine_kraft(c2))
    print(sum_ine_kraft(c3))
    print(sum_ine_kraft(c4))
    print(sum_ine_kraft(c5))
    print(sum_ine_kraft(c6))
    # print(sum_ine_kraft(c7))
    # print(sum_ine_kraft(c8))

    print("--------Punto 8-----------")
    c9 = ["==", "<", "<=", ">", ">=", "<>"]
    c10 = [")", "[]", "]]", "([", "[()]", "([)]"]
    c11 = ["/", "*", "-", "*", "++", "+-"]
    c12 = [".,", ";", ",,", ":", "...", ",:;"]

    print(sum_ine_kraft(c9))
    print(sum_ine_kraft(c10))
    print(sum_ine_kraft(c11))
    print(sum_ine_kraft(c12))

