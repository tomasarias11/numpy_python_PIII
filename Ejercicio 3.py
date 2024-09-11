# Ejercicios con comprensión de listas

from random import random
import random

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")

    # Práctica de comprensión de listas
    # 1) Generar una lista con números del 0 al 10 inclusive

    lista_0_10 = [x for x in range(11)]
    print('Lista del 0 al 10:', lista_0_10)

    # 2) Generar la tabla del 5 (desde 0*5 hasta 10*5)

    tabla_5 = [x * 5 for x in range(11)]
    print('Tabla del 5:', tabla_5)

    # 3) Generar una lista de 10 números aleatorios entre 1 y 30
    
    dias_mes = [random.randint(1, 30) for _ in range(10)]
    print('Números aleatorios entre 1 y 30:', dias_mes)

    print("terminamos")

    input("Muchas gracias por revisarlo")