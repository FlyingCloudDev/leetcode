# Tiene una complejidad de tiempo O(N^2) en el peor y promedio caso.

def bubble_sort(array):
    
    n = len(array)
   
    for i in range(n):
        # i cuenta el numero de vuelta, n la cantidad de vueltas
        for j in range(0, n-i-1):
            # j toma el valor del indice(desde el 0), y el rango es (de cero, hasta 7 - 0 - 1) = 6 (en la primer vuelta)
            # entonces toma valores desde los indices 0 hasta el 5 (ya que range toma hasta el numero previo al ultimo valor)
            # i va aumentando en cada iteración
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == '__main__':
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array desordenado:")
    print(data)
    bubble_sort(data)
    print("\nArray ordenado:")
    print(data)

    #