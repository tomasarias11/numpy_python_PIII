# Ejercicios con lambda
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    palabras = ['love', 'casa', 'programacion']

    # Lambda expression
    # 1) Realizar una función lambda que retorne el tamaño (len) de un string pasado como parámetro
    
    len_string = lambda x: len(x)
    
    print('El tamaño del string "jesus gonzalez" es:', len_string('jesus gonzalez'))

    # 2) Utilice la función map para mapear una lambda expression que retorne el tamaño (len) de cada texto 
    # en cada iteración de la lista de textos
    
    # Usando la lambda definida anteriormente con map
    palabras_len = list(map(len_string, palabras))

    print('Lista de longitudes de palabras usando la lambda "len_string":', palabras_len)

    # Alternativamente, usando una lambda "in line" dentro del map
    palabras_len = list(map(lambda x: len(x), palabras))

    print('Lista de longitudes de palabras usando lambda dentro del map:', palabras_len)

    print("terminamos")

    input("Muchas garcias por revisarlo") 