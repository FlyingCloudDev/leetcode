# Given an integer array NUMS, return TRUE if any value appears AT LEAST TWICE in the array, and return FALSE if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: True

# Example 2:
# Input: nums = [1,2,3,4]
# Output: False

# Complejidad de Tiempo Lineal: O(n)

numeros = [1,2,3,4,5,6,1]

def solution(nums):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True
    
print(solution(numeros))

# los SETS en python son un tipo de dato primitivo que no permite duplicados dentro de sus elementos, esto hace que al pasar el array a set, sea de complejidad lineal O(n), ya que los pasa una vez, otra solucion sería un for dentro de un for para comparar los elementos entre todos, pero sería muchisimo menos eficiente, ya que sería cuadrático O(n^2).
# Los SETS se implementan como TABLAS HASH, por lo que para buscar, insertar y borrar, se puede realizar en O(1)