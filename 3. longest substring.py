class Solution(object):
    @classmethod
    def lengthOfLongestSubstring(self, s):
        # Puntero que ira por la derecha y variable que almacena 
        # La mayor longitud de subcadena encontrada
        left = mayor_longitud_cadena = 0 
        char_set = set() # Set que almacenara la cadena actual sin caracteres repétidos
        
        # Iterando la cadena
        for right in range(len(s)): 
            while s[right] in char_set: # Verificando que el caracter no se encuentre en la cadena actual
                char_set.remove(s[left]) # Removimiendo los caracteres del puntero de la izquierda, hasta el caracter que esta repetido
                left += 1 

            char_set.add(s[right]) # Se agrega el caracter al set
            mayor_longitud_cadena = max(mayor_longitud_cadena, right - left + 1) # Toma la mayor longitud de entre 2 variables

        return mayor_longitud_cadena

if __name__ == "__main__":
    lenght = Solution.lengthOfLongestSubstring('asjrgapa"')
    print(lenght)