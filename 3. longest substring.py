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
    def iterar_cadena_principal(self, inicio, fin, paso, s):
        lista_subcadenas = []
        cadena = []

        for i in range(inicio, fin, paso):
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
        cadena_mayor = Solution.comparar_longitud(lista_subcadenas)
        return cadena_mayor

    @classmethod
    def lengthOfLongestSubstring(self, s):
        Cadena_mayor_longitud = 0

        if len(s) == 0: # Caso en el que la longitud sea de 0
            return 0
        elif len(s) == 1: # Caso en el que la longitud de la cadena sea de 1
            return 1
        
        # Iterando la cadena
        for i in range(0, len(s), 1): # Se itera la cadena cada vez iniciando desde un inidice mayor
            if Cadena_mayor_longitud < len(s) - i: # Verifica si es posible encontrar una subcadena mas larga que la actual
                cadena_mayor_temporal = Solution.iterar_cadena_principal(i, len(s), 1, s)
                if cadena_mayor_temporal > Cadena_mayor_longitud: # Verifica si la subcadena nueva es mayor que la antigua
                    Cadena_mayor_longitud = cadena_mayor_temporal
        return Cadena_mayor_longitud

if __name__ == "__main__":
    lenght = Solution.lengthOfLongestSubstring('asjrgapa"')
    print(lenght)