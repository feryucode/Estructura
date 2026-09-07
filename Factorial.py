import time
inicio = time.time()
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Bloque principal de ejecución
if __name__ == "__main__":
    a = 5
    print(factorial(a))

    fin = time.time()
    tiempo_total = fin - inicio
    print(f"Tiempo total: {tiempo_total}")
    