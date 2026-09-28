def fibonacci_con_contador(n):
    a, b = 0, 1
    for i in range(1, n + 1):
        print(f"{i}: {a}")
        a, b = b, a + b

fibonacci_con_contador(500)
