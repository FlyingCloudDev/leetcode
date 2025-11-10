# O(n!) example

def generar_permutaciones_factorial(arr, l=0):
    # Genera todas las permutaciones posibles de una lista.
    # Complejidad: O(N * N!) (Tiempo para generar e imprimir todas las permutaciones)

    # Caso Base: Cuando llegamos al final de la lista, una permutación está completa.
    if l == len(arr):
        # Esta operación (imprimir/guardar) se realiza N! veces.
        print(arr) 
        return
    # La clave de O(N!): En cada nivel 'l' de la recursión, hay (N-l) opciones para el elemento actual.
    # El bucle interno for ejecuta el paso recursivo (N-l) veces.
    for i in range(l, len(arr)):
        # 1. Intercambio: Colocamos el elemento 'i' en la posición 'l'
        arr[l], arr[i] = arr[i], arr[l]
        # 2. Llamada Recursiva: Pasamos al siguiente elemento (l+1)
        generar_permutaciones_factorial(arr, l + 1)
        # 3. Retroceso (Backtracking): Deshacemos el intercambio para el siguiente bucle.
        # Esto asegura que la lista original se restaure para la siguiente iteración del for.
        arr[l], arr[i] = arr[i], arr[l]

# --- Prueba del Crecimiento ---
lista_corta = [1, 2, 3] # N=3
print("--- Permutaciones (N=3): 3! = 6 ---")
generar_permutaciones_factorial(lista_corta)
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 2, 1]
# [3, 1, 2]
# Este algoritmo toma 6 pasos principales.