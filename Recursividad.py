def completar_tareas(tarea, nivel=0):
    """
    Función recursiva que procesa tareas. Si encuentra una subtarea, 
    se llama a sí misma aumentando el nivel de profundidad.
    """
    sangria = "   " * nivel  # Espaciado para visualizar la profundidad
    
    # Caso base: Si la tarea es un texto simple, simplemente la "hacemos"
    if isinstance(tarea, str):
        print(f"{sangria}✅ Completado: {tarea}")
        return 1  # Retornamos 1 indicando que se completó una tarea
        
    # Caso recursivo: Si la tarea es una lista (subtareas anidadas)
    elif isinstance(tarea, list):
        total_completadas = 0
        for subtarea in tarea:
            # Recursividad: La función se invoca a sí misma para resolver la subtarea
            total_completadas += completar_tareas(subtarea, nivel + 1)
        return total_completadas

# Estructura de la vida diaria: Tareas principales que contienen listas de subtareas
rutina_diaria = [
    "Levantarse y tender la cama",
    [
        "Preparar el desayuno",
        [
            "Hervir agua",
            "Preparar café",
            "Hacer huevos revueltos"
        ]
    ],
    "Revisar correos del trabajo",
    [
        "Limpieza profunda del hogar",
        [
            "Barrer la sala",
            "Lavar la ropa",
            [
                "Separar ropa blanca y de color",
                "Poner jabón en la lavadora",
                "Tender la ropa al sol"
            ]
        ]
    ]
]

# Ejecución del código
print("--- INICIANDO RUTINA DIARIA ---")
total_tareas = completar_tareas(rutina_diaria)
print("-" * 31)
print(f"¡Día terminado! Has completado un total de {total_tareas} tareas individuales.")