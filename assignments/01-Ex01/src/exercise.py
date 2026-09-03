def main():
    """
    Realiza un programa que sea útil para determinar si los números enteros X, Y y Z, proporcionados por el usuario, son medidas correctas para los lados de un triángulo y si lo son, debe decir si se trata de un triángulo Equilátero, Isósceles o Escaleno.

    NOTA: X, Y y Z son los lados de un triángulo si cumplen con las siguientes condiciones:

    Todos los números deben ser mayores que cero.
    X + Y > Z
    X + Z > Y
    Y + Z > X
    es decir, la suma de dos de las medidas debe ser estrictamente mayor que la tercera.

    El triángulo equilátero tiene 3 lados iguales, el isósceles tiene 2 lados iguales y el escaleno tiene los 3 lados diferentes.
    """

    x = int(input("Ingrese el primer lado del triángulo: "))
    y = int(input("Ingrese el segundo lado del triángulo: "))
    z = int(input("Ingrese el tercer lado del triángulo: "))

    if not(x > 0 and y > 0 and z > 0):
        print("NO ES UN TRIÁNGULO")
    elif x + y > z or x + z > y or y + z > x:
        if x == y and y == z:
            print("EQUILÁTERO")
        elif x == y or x == z or y == z:
            print("ISÓSCELES")
        else:
            print("ESCALENO")
    else:
        print("NO ES UN TRIÁNGULO")

if __name__=='__main__':
    main()
