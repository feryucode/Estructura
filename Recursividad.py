import sys

# Mostramos el límite de seguridad que tiene Python por defecto
print(f"Límite de recursividad estándar de Python: {sys.getrecursionlimit()} niveles\n")

# 1. GENERAMOS LA PROFUNDIDAD (1500 cajas, una dentro de otra)
caja_misteriosa = "🎁 Regalo Final"
for _ in range(1500):
    # Metemos la caja actual dentro de una nueva caja (una nueva lista)
    caja_misteriosa = [caja_misteriosa] 

# 2. FUNCIÓN RECURSIVA
def abrir_caja(caja, nivel=1):
    # Caso base: Encontramos el texto final
    if isinstance(caja, str):
        print(f"\n¡ÉXITO! Encontramos el {caja} en el nivel {nivel}.")
        return nivel
    
    # Caso recursivo: Si es una lista, la abrimos y pasamos a la siguiente
    else:
        if nivel % 200 == 0:
            print(f"Desempacando caja nivel {nivel}...")
        
        # Aquí la función se llama a sí misma bajando un nivel más
        return abrir_caja(caja[0], nivel + 1)

# 3. PRIMER INTENTO (Va a chocar con la pared de seguridad de Python)
print("--- INTENTO 1: SIN MODIFICAR EL LÍMITE ---")
try:
    abrir_caja(caja_misteriosa)
except RecursionError as error:
    print(f"\n💥 ¡BUM! PYTHON SE DETUVO.")
    print(f"Mensaje oficial del sistema: {error}")
    print("Explicación: Llegamos al nivel 1000 de anidación. Python cortó el proceso para evitar un 'Stack Overflow' y no saturar tu memoria RAM.\n")

# 4. SEGUNDO INTENTO (Hackeando el límite)
print("--- INTENTO 2: HACKEANDO EL LÍMITE DE PYTHON ---")
sys.setrecursionlimit(2500)  # Forzamos a Python a soportar 2500 niveles de profundidad
print(f"Nuevo límite ajustado a: {sys.getrecursionlimit()} niveles")
print("Intentando abrir de nuevo...\n")

abrir_caja(caja_misteriosa)