# O(n log n) example:

def merge_sort(array):

    # FASE 1: DIVISIÓN (O(log N))
    if len(array) <= 1:
        # CASO BASE: si el array tiene 0 o 1 elemento, se considera ordenado
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # LLAMADAS RECURSIVAS: estas lineas hacen la DIVISION
    merge_sort(left_part)
    merge_sort(right_part)

    # no se llega hasta acá hasta que el array esté descompuesto en unidades
    # FASE 2: MEZCLA (MERGE) Y ORDENACIÓN (O(N) por nivel)
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # 1. Bucle Principal de Mezcla y Ordenación
    # Este 'while' recorre y compara los elementos de las dos sublistas (left_part y right_part).
    # Mientras ambas tengan elementos, compara el elemento más pequeño de cada una 
    # y coloca el menor en el 'array' original.
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1
    # 2. Bucle para residuos (Copia los elementos restantes de la izquierda)
    # Una vez que una de las sublistas se agota, esta línea se encarga de copiar
    # los elementos restantes de la otra sublista (que ya están ordenados).
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    # 3. Bucle para residuos (Copia los elementos restantes de la derecha)
    # Lo mismo que arriba, pero para la sublista derecha.
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