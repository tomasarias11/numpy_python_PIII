# Ejercicios con lambda
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    numeros = [1, -5, 4, 3]
    
    # Lambda expression
    # 1) Realizar una funcion lambda que eleve al cuadrado el número pasado como parámetro
    
    potencia_2 = lambda x: x**2
    pot_3 = potencia_2(3)

    print('El número 3 elevado al cuadrado es:', pot_3)  

    # 2) Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista "numeros"

    # Usando la lambda definida anteriormente con map
    numeros_map = map(potencia_2, numeros)
    numeros_map = list(numeros_map)  

    print('Lista de números elevados al cuadrado usando la lambda "potencia_2":', numeros_map)

    # Usando una lambda "in line" dentro del map
    numeros_lambda = list(map(lambda x: x**2, numeros))

    print('Lista de números elevados al cuadrado usando lambda dentro del map:', numeros_lambda)

    print("terminamos")
    
    input("Muchas gracias por revisarlo")