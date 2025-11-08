# Binary search O(log n) example.

def busqueda_binaria(lista_ordenada, objetivo):
    inicio = 0
    fin = len(lista_ordenada) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2 
        valor_medio = lista_ordenada[medio]
        
        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1    
    return -1

# LA LISTA DEBE ESTAR ORDENADA para que la búsqueda binaria funcione(este caso n=10).
mi_lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# Caso 1: Encontrar un número que sí está (23)
numero_buscado_1 = 23
indice_1 = busqueda_binaria(mi_lista, numero_buscado_1)
print(f"El {numero_buscado_1} está en el índice: {indice_1}")
# Caso 2: Encontrar un número que no está (40)
numero_buscado_2 = 40
indice_2 = busqueda_binaria(mi_lista, numero_buscado_2)
print(f"El {numero_buscado_2} está en el índice: {indice_2}")

# La complejidad logaritmica de O(log n) hace que el tiempo de ejecución aumente MUY LENTAMENTE con el aumento del tamaño de los datos (n), ya que el algoritmo constantemente va descartando una gran parte de los datos en cada paso (generalmente la midad de los datos).
# Esto lo convierte en un algritmo altamente eficiente.