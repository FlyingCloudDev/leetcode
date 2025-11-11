# given an array nums of N integers where nums[i] is in the range (1,n), return an array of all the integers in the range (1,n) that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

# Complejidad de Tiempo Lineal: O(n)
nums = [4,3,2,7,8,2,3,1]
set_nums = set(nums) # [4,3,2,7,8,1]
lista = []

def solution(nums):
    for i in range(1, len(nums) +1):
        if i not in set_nums:
            lista.append(i)
    return lista

# Se itera sobre el rango y se agregan los numeros a "lista" si no estaban en set_nums.
