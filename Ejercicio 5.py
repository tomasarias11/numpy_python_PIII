# Ejercicios con comprensión de listas

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Lista de accesos al molinete
    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # 1) Filtrar los ID de personal entre 1 y 10 inclusive
    
    personal_1_10 = [x for x in accesos if 1 <= x <= 10]

    print('Personal del 1 al 10:', personal_1_10)
    print('La cantidad de personal con ID entre 1 y 10 es:', len(personal_1_10))

    # 2) Filtrar los ID que están en la lista de ID válidos
    
    id_validos = [3, 4, 7, 8, 15]
    
    personal_valido = [x for x in accesos if x in id_validos]

    print('Personal con acceso válido:', personal_valido)

    print("terminamos")

    lista = [x**2 for x in range(5)]
    
    print(lista)

    input("Muchas gracias por revisarlo")