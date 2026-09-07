import random
import statistics

# 1. Generar 50 números al azar del 1 al 100
numeros = [random.randint(150, 250) for _ in range(50)]

# 2. Calcular las métricas estadísticas
media = statistics.mean(numeros)
mediana = statistics.median(numeros)

# Usamos multimode por si existe más de una moda con la misma frecuencia
moda = statistics.multimode(numeros) 

# Desviación estándar y varianza muestral (las más comunes en estadística)
desviacion_estandar = statistics.stdev(numeros)
varianza = statistics.variance(numeros)

# 3. Mostrar los resultados
print("=== DATOS GENERADOS ===")
print(numeros)
print("\n=== ANÁLISIS ESTADÍSTICO ===")
print(f"Media:              {media:.2f}")
print(f"Mediana:            {mediana:.2f}")
print(f"Moda(s):            {moda}")
print(f"Desviación Estándar:{desviacion_estandar:.2f}")
print(f"Varianza:           {varianza:.2f}")
