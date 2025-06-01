
'''
Tomo cada letra de la cadena y voy creando subcadenas que no tengan letras repetidas.
Luego esas subcadenas las guardo en una lista y al final devuelvo la longitud de la subcadena más larga.
Condiciones:
La letra que se vaya a agregar no debe de estar repetida en la cadena que se esta creando
'''

def devolverCadena(listaLetras):
    cadena = ''
    for letra in listaLetras:
        cadena += letra
    return cadena

def lengthOfLongestSubstring(s):
    lista_subcadenas = []
    cadena = []

    # Iterando la cadena principal
    for i, letra in enumerate(s):
        # Verifica que si es la ultima letra en la cadena principal en ser recorrida
        if i == len(s)-1 or letra in cadena:
            cadena_completa = devolverCadena(cadena) # Devuelve la cadena como un string completo
            lista_subcadenas.append(cadena_completa) # Agregas la cadena a la lista de subcadenas

            if letra in cadena:
                cadena.clear()
                cadena.append(letra)
        # Verficar que la letra no sea repetida
        elif not letra in cadena:
            cadena.append(letra) # Se agrega la letra a la lista que simula la cadena
    
    # Comparar la longitud de las subcadenas almacenadas
    cadena_mas_larga = lista_subcadenas[0]
    for subcadena in lista_subcadenas:
        if len(subcadena) > len(cadena_mas_larga):
            cadena_mas_larga = subcadena
    print(cadena_mas_larga)
    return len(cadena_mas_larga) # Devolviendo la longitud de la subcadena mas larga


if __name__ == "__main__":
    lenght = lengthOfLongestSubstring('abcabcbb')
    print(lenght)