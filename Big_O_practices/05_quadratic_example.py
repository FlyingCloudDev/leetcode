# Tiene una complejidad de tiempo O(N^2) en el peor y promedio caso.

def bubble_sort(array):
    
    n = len(array)
   
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == '__main__':
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array desordenado:")
    print(data)
    bubble_sort(data)
    print("\nArray ordenado:")
    print(data)