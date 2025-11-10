# O(2^n) example

def fibonacci_exponencial(n):
    # Calcula el N-ésimo número de Fibonacci usando recursión ingenua.
    # Complejidad: O(2^N) - Muy ineficiente debido a la repetición de cálculos. 
    if n <= 1:
        return n
    # La clave de la complejidad O(2^N): Por cada paso (N), se generan dos nuevas llamadas recursivas.
    return fibonacci_exponencial(n - 1) + fibonacci_exponencial(n - 2)

# Prueba:
# Para N=40, una computadora tardaría una cantidad notable de tiempo
# mientras que para N=50 podría tardar varios minutos o más, dependiendo del sistema.
print(f"Fibonacci(8) = {fibonacci_exponencial(8)}")
print(f"Fibonacci(10) = {fibonacci_exponencial(10)}")

# O(n) comparación
def fibonacci_lineal(n):
    # Calcula el N-ésimo número de Fibonacci usando Programación Dinámica (Iteración).
    # Complejidad: O(N) - Extremadamente eficiente.
    if n <= 1:
        return n
    # Almacenamos los dos últimos valores de la secuencia.
    a = 0  # F(0)
    b = 1  # F(1)
    # El bucle corre N-1 veces. 
    # Cada iteración toma tiempo constante O(1).
    for _ in range(2, n + 1):
        # 1. Calculamos el siguiente número: F(i) = F(i-1) + F(i-2)
        next_fib = a + b
        # 2. Actualizamos los valores para la siguiente iteración.
        # El antiguo 'b' se convierte en el nuevo 'a' F(i-2) -> F(i-1)
        a = b
        # El resultado 'next_fib' se convierte en el nuevo 'b' F(i-1) -> F(i)
        b = next_fib

    # Al final del bucle, 'b' contiene el resultado F(n)
    return b
# --- Contraste de Eficiencia ---
# Para N=40
# O(2^N): Haría miles de millones de operaciones.
# O(N): Haría solo 40 operaciones.

print(f"Fibonacci Lineal(40) = {fibonacci_lineal(40)}")
