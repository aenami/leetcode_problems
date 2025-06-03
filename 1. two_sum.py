import array as arr

'''
Se inicia iterando sobre el array dado. Sobre la iteracion se verifica que el primer numero 
que se va a elegir para buscar la suma de dos numeros que resulten en target no sea igual ni
mayor a este.

Si target es impar y el primer numero elegido es impar: El 2do numero debe ser la resta entre target 
y el 1er numero (PREGUNTA, IF RESTA ENTRE TARGET Y EL 1ER NUMERO IN NUMS?)
SI LO ESTA, AHI ESTARIA LA COMBINACION, SINO, PASA CON LA SIGUIENTE ITERACION

Si target es impar y el primero numero elegido es par: 
'''

class Solution:
    @classmethod
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Nueva lista con valores los cuales si sean relevantes
        lista_modificada = [n for n in nums if n < target] 
        for numero in lista_modificada: # Recorriendo la nueva lista
            lista_sin_numero = lista_modificada.copy()
            index = lista_sin_numero.index(numero) # Lista que no incluye el numero actual que se esta recorriendo
            lista_sin_numero[index] = 0
            # Verifico si el numero requerido para la suma se encuentra en la lista
            if target-numero in lista_sin_numero: 
                print(f'Lista sin numero:{lista_sin_numero}')
                return [lista_modificada.index(numero), lista_sin_numero.index(target-numero)]

if __name__ == "__main__":
    # Un array solo puede almacenar valores de un mismo tipo
    array = arr.array('i',[3,3]) # Inicializando el array
    target = 6
    print(Solution.twoSum(array, target))
