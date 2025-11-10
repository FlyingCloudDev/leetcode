# O(1) example

mi_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # N=10

# 1. Acceder al elemento O(1)
tercer_elemento = mi_lista[2] # Siempre tarda lo mismo, sin importar el tamaño de la lista

# 2. Modificar el elemento O(1)
mi_lista[5] = 999 # La asignación es instantánea

print(f"Elemento accedido: {tercer_elemento}")
print(f"Lista modificada: {mi_lista}")

# el tiempo de la operación no depende del tamaño de datos(n), ya que el sistema de gestion de memoria sabe donde comienza la lista y que cada elemento tiene un tamaño fijo, Para encontrar el elemneto en el índice "I", sólo necesita realizar un calculo de un solo paso, y es el mismo si la lista tiene 4 elementos o 2 millones.