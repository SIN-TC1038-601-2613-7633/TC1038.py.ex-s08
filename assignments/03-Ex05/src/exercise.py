def main():
    """
    Escribe un programa que calcule el IMC (Índice de Masa Corporal) de una persona, el cual se utiliza para determinar si la proporción de peso y altura es adecuada. El IMC se puede calcular utilizando la siguiente fórmula:

    indice = peso / altura**2

    Donde el peso debe darse en kilogramos y la altura en metros. La siguiente tabla muestra cómo se clasifican los diferentes rangos de índice:

    Rango de índice          Descripción

    índice < 20                  'PESO BAJO'

    20 <= índice < 25        'NORMAL'

    25 <= índice < 30        'SOBREPESO'

    30 <= índice < 40        'OBESIDAD'

    índice >= 40                'OBESIDAD MORBIDA'
    """
    peso = float(input())
    altura = float(input())
    indice = peso / altura**2
    if indice < 20:
        print('PESO BAJO')
    elif indice >= 20 and indice < 25:
        print('NORMAL')
    elif indice >= 25 and indice < 30:
        print('SOBREPESO')
    elif indice >= 30 and indice < 40:
        print('OBESIDAD')
    else:
        print('OBESIDAD MORBIDA')
if __name__=='__main__':
    main()
