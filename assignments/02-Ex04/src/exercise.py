def main():
    """
    Realiza un programa que ordena en forma ascendente tres números enteros x, y, z.

    IMPORTANTE: NO puedes utilizar la función incorporada de Python: sort(), utiliza estatutos de comparación.
    """
    x = int(input())
    y = int(input())
    z = int(input())

    if x <= y and x <= z:
        if y <= z:
            print(x)
            print(y)
            print(z)
        else:
            print(x)
            print(z)
            print(y)
    elif y <= x and y <= z:
        if x <= z:
            print(y)
            print(x)
            print(z)
        else:
            print(y)
            print(z)
            print(x)
    else:
        if x <= y:
            print(z)
            print(x)
            print(y)
        else:
            print(z)
            print(y)
            print(x)

if __name__=='__main__':
    main()
