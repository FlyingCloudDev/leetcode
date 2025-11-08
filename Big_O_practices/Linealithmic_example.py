# O(n log n) example:

def merge_sort(array):

    # CASO BASE DE LA RECURSION: Una lista con 0 o 1 elemento ya está ordenada.
    # Esto define el límite de las divisiones (la altura del árbol es log N).
    if len(array) <= 1:
        return
    
    # DIVIDIR: Encontrar el punto medio y crear las dos mitades.
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # LLAMADAS RECURSIVAS: Se sigue dividiendo cada mitad hasta llegar al caso base.
    # El número total de veces que estas llamadas pueden anidarse es O(log N).
    merge_sort(left_part)
    merge_sort(right_part)

    # Inicialización de índices para las partes izquierda, derecha y la lista original.
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # MEZCLAR (Merge): Compara los elementos de las dos mitades y los coloca en el array original en orden.
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # MANEJAR RESIDUOS: Si alguna mitad tiene elementos restantes ya ordenados, se copian al final del array original.
    # Copia elementos restantes de la mitad izquierda.
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    # Copia elementos restantes de la mitad derecha
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))

    # O(N log N) es EXELENTE, es la complejidad más eficiente que se puede alcanzar para la mayoría de los algoritmos de ORDENAMIENTOS BASADOS EN COMPARACIONES. Es significativamente más rápido que O(N^2)(Buble Sort) y apenas un poco más lento que O(N) para valores de N muy grandes.