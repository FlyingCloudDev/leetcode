
example = [1,3,10,20,2,7]

def linear_example(list):
    for number in list:
        if number == 2:
            return True
    return False

print(linear_example(example))

# Para recorrer toda la lista y asegurarnos que el numero "N = 2" está o no en la lista, nos tardaría "N tiempo". Necesitamos chequear cada numero en la lista por lo menos una vez.
# Haciendo que esta solucion sea "O(N)", osea, mientras más grande sea "N", más tiempo va a tardar el algoritmo.