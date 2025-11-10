# Given an array nums containing N distinct numbers in the range (0, N), return the ONLY NUMBER in the range that is missing from the array

# Example 1:
# Input: nums = [3,0,1]
# Output: 2 (since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.)

# Example 2:
# Input: nums = [0,1]
# Output: 2 (since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.)

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8 (since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.)

# Complejidad de Tiempo Lineal: O(n)
def find_missing_number(nums):
    
    # Utiliza el método de la suma (suma esperada - suma real). 
    N = len(nums)

    suma_esperada = sum(range(N + 1))
    suma_real = sum(nums)
    missing_number = suma_esperada - suma_real
    
    return missing_number

# Esto solamente funciona en estos casos ya que todos los numeros son secuenciales y se saben sus valores de inicio y de final(este se puede calcular)

# --- Pruebas con los Ejemplos ---
ejemplo1 = [3, 0, 1]
ejemplo2 = [0, 1]
ejemplo3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]

print(f"Array: {ejemplo1} -> Número faltante: {find_missing_number(ejemplo1)}")
# Output esperado: 2
print(f"Array: {ejemplo2} -> Número faltante: {find_missing_number(ejemplo2)}")
# Output esperado: 2
print(f"Array: {ejemplo3} -> Número faltante: {find_missing_number(ejemplo3)}")
# Output esperado: 8

