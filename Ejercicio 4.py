# Ejercicios con comprensión de listas

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Utilizar comprensión de listas con condicionales
    # 1) Convertir lista de str a int, reemplazando no numéricos por 0
    # usando isdigit para verificar si son números válidos

    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']

    # Usamos try-except para manejar valores no numéricos
    lista_numeros = [int(x) if x.isdigit() else 0 for x in list_numeros_str]
    print("Lista convertida (sin números negativos):", lista_numeros)

    # Probar con números negativos
    list_numeros_str = ['-5', '-2', '3', '', '7', 'NaN']

    # Para manejar números negativos, chequeamos manualmente si el número es válido
    lista_numeros = [int(x) if x.lstrip('-').isdigit() else 0 for x in list_numeros_str]
    print("Lista convertida (con números negativos):", lista_numeros)

    print('isdigit no detecta signos negativos correctamente')

    print("terminamos")

    input("Muchas gracias por revisarlo")