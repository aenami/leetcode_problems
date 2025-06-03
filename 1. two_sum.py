import array as arr
'''
Itero sobre el array original. Creo una lista copia del array original que es con la que trabajare
en cada iteracion. En esta lista sobreescribo el numero actual que estoy recorriendo, por uno
el cual se que nunca sera igual al numero necesario que al ser sumado con el actual que se esta 
iterando llegara a ser igual a target.
Luego verifico si el numero que al ser sumado con el actual que estoy recorriendo resulte en target
se encuentra en la lista.
Si lo esta entonces ya retorno los indices de dichos numeros.
'''
class Solution:
    @classmethod
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for numero in nums: # Recorriendo la lista
            nums_copy = list(nums)
            index = nums.index(numero) 
            nums_copy[index] = target-numero+1 # Lista que excluye al numero actual
            # Verifico si el numero requerido para la suma se encuentra en la copia de la lista
            if target-numero in nums_copy:
                return [index, nums_copy.index(target-numero)]
if __name__ == "__main__":
    # Un array solo puede almacenar valores de un mismo tipo
    array = arr.array('i',[3,3]) # Inicializando el array
    target = 6
    print(Solution.twoSum(array, target))