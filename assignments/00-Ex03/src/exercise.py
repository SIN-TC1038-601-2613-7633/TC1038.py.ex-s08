def main():
    """
    Programa que muestre el mayor de 3 números enteros x, y, z proporcionados por el usuario.
    """

    x = int(input())
    y = int(input())
    z = int(input())

    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)

if __name__ == '__main__':
    main()
