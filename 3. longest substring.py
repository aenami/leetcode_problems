
'''
Tomo cada letra de la cadena y voy creando subcadenas que no tengan letras repetidas.
Luego esas subcadenas las guardo en una lista y al final devuelvo la longitud de la subcadena más larga.
Condiciones:
La letra que se vaya a agregar no debe de estar repetida en la cadena que se esta creando
'''

class Solution(object):
    @classmethod
    def devolverCadena(self, listaLetras):
        cadena = ''
        for letra in listaLetras:
            cadena += letra
        return cadena
    
    @classmethod
    def comparar_longitud(self, lista_de_subcadenas):
        # Comparar la longitud de las subcadenas almacenadas
        print(lista_de_subcadenas)
        cadena_mas_larga = lista_de_subcadenas[0]

        for subcadena in lista_de_subcadenas:
            if len(subcadena) > len(cadena_mas_larga):
                cadena_mas_larga = subcadena
        print('Valores finales')
        print(cadena_mas_larga)
        return len(cadena_mas_larga) # Devolviendo la longitud de la subcadena mas larga

    @classmethod
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0: # Caso en el que la longitud sea de 0
            return 0
        elif len(s) == 1: # Caso en el que la longitud de la cadena sea de 1
            return 1

        lista_subcadenas = []
        cadena = []

        # Iterando la cadena principal por la izquierda
        for i, letra in enumerate(s):
            # Caso final en el que no hayan letras repetidas en la cadena
            if i == len(s)-1 and len(lista_subcadenas) == 0 and not letra in cadena or not letra in cadena and i == len(s)-1:
                cadena.append(letra) 
                cadena_completa = Solution.devolverCadena(cadena) 
                lista_subcadenas.append(cadena_completa)
            # Verifica si es la ultima letra en la cadena principal en ser recorrida
            elif i == len(s)-1 and letra in cadena:
                cadena_completa = Solution.devolverCadena(cadena) # Devuelve la cadena 
                lista_subcadenas.append(cadena_completa) # Agregas la cadena a la lista 
            elif letra in cadena: # Verifica si la letra esta repetida en la cadena actual
                cadena_completa = Solution.devolverCadena(cadena)
                lista_subcadenas.append(cadena_completa) 
                cadena.clear()
                cadena.append(letra)
            # Verficar que la letra no sea repetida
            elif not letra in cadena:
                cadena.append(letra) # Se agrega la letra a la lista que simula la cadena
        
        # Funcion que devolvera la longitud de cadena mas larga
        cadena_mayor1 = Solution.comparar_longitud(lista_subcadenas)

        lista_subcadenas = []
        cadena = []
        
        # Iterando la cadena principal por la derecha
        for i in range(len(s)-1, -1, -1):
            # Caso final en el que no hayan letras repetidas en la cadena
            if i == len(s)-1 and len(lista_subcadenas) == 0 and not s[i] in cadena or not s[i] in cadena and s[i] == len(s)-1:
                cadena.append(s[i]) 
                cadena_completa = Solution.devolverCadena(cadena) 
                lista_subcadenas.append(cadena_completa)
            # Verifica si es la ultima letra en la cadena principal en ser recorrida
            elif i == len(s)-1 and s[i] in cadena:
                cadena_completa = Solution.devolverCadena(cadena) # Devuelve la cadena 
                lista_subcadenas.append(cadena_completa) # Agregas la cadena a la lista 
            elif s[i] in cadena: # Verifica si la letra esta repetida en la cadena actual
                cadena_completa = Solution.devolverCadena(cadena)
                lista_subcadenas.append(cadena_completa) 
                cadena.clear()
                cadena.append(s[i])
            # Verficar que la letra no sea repetida
            elif not s[i] in cadena:
                cadena.append(s[i]) # Se agrega la letra a la lista que simula la cadena
        
        # Funcion que devolvera la longitud de cadena mas larga
        cadena_mayor2 = Solution.comparar_longitud(lista_subcadenas)

        if cadena_mayor1 > cadena_mayor2:
            return cadena_mayor1
        elif cadena_mayor2 > cadena_mayor1:
            return cadena_mayor2
        else:
            return cadena_mayor1

if __name__ == "__main__":
    lenght = Solution.lengthOfLongestSubstring('dvdf')
    print(lenght)