import bisect


class NodoIngrediente:
    def __init__(self, nombre: str):
        self.nombre = nombre.strip().capitalize()
        self.siguiente = None


class Postre:
    def __init__(self, nombre: str):
        self.nombre = nombre.strip().title()
        self.cabeza_ingredientes = None


class GestorPostres:
    def __init__(self):
        self.postres: list[Postre] = []

    def _buscar_indice_postre(self, nombre_postre: str) -> int:
        objetivo = nombre_postre.strip().title()
        for i, postre in enumerate(self.postres):
            if postre.nombre == objetivo:
                return i
        return -1

    def imprimir_ingredientes(self, nombre_postre: str) -> None:
        if not self.postres:
            print("[!] Caso verificado: El arreglo POSTRES está completamente vacío.")
            return

        idx = self._buscar_indice_postre(nombre_postre)
        if idx == -1:
            print(f"[!] Caso verificado: El postre '{nombre_postre}' no existe en el arreglo.")
            return

        postre = self.postres[idx]
        actual = postre.cabeza_ingredientes

        if actual is None:
            print(f"[i] El postre '{postre.nombre}' está registrado, pero su lista apunta a NIL (sin ingredientes).")
            return

        ingredientes = []
        while actual is not None:
            ingredientes.append(actual.nombre)
            actual = actual.siguiente

        print(f"\nIngredientes de '{postre.nombre}':")
        print(" -> ".join(ingredientes) + " -> NIL")

    def insertar_ingredientes(self, nombre_postre: str, nuevos_ingredientes: list[str]) -> None:
        if not self.postres:
            print("[!] Caso verificado: El arreglo POSTRES está vacío. Dé de alta un postre primero.")
            return

        idx = self._buscar_indice_postre(nombre_postre)
        if idx == -1:
            print(f"[!] Caso verificado: El postre '{nombre_postre}' no se encontró.")
            return

        if not nuevos_ingredientes:
            print("[!] Caso verificado: No se proporcionaron ingredientes para insertar.")
            return

        postre = self.postres[idx]

        for ing in nuevos_ingredientes:
            ing_limpio = ing.strip().capitalize()
            if not ing_limpio:
                continue

            nuevo_nodo = NodoIngrediente(ing_limpio)

            if postre.cabeza_ingredientes is None:
                postre.cabeza_ingredientes = nuevo_nodo
                print(f"[+] '{ing_limpio}' insertado como primer ingrediente de '{postre.nombre}'.")
                continue

            actual = postre.cabeza_ingredientes
            duplicado = False
            while True:
                if actual.nombre.lower() == ing_limpio.lower():
                    print(f"[!] Caso verificado: El ingrediente '{ing_limpio}' ya existe en '{postre.nombre}'.")
                    duplicado = True
                    break
                if actual.siguiente is None:
                    break
                actual = actual.siguiente

            if not duplicado:
                actual.siguiente = nuevo_nodo
                print(f"[+] '{ing_limpio}' agregado al final de la lista de '{postre.nombre}'.")

    def eliminar_ingrediente(self, nombre_postre: str, nombre_ingrediente: str) -> None:
        if not self.postres:
            print("[!] Caso verificado: El arreglo POSTRES está vacío.")
            return

        idx = self._buscar_indice_postre(nombre_postre)
        if idx == -1:
            print(f"[!] Caso verificado: El postre '{nombre_postre}' no existe.")
            return

        postre = self.postres[idx]
        actual = postre.cabeza_ingredientes

        if actual is None:
            print(f"[!] Caso verificado: '{postre.nombre}' no tiene ingredientes para eliminar (apunta a NIL).")
            return

        objetivo = nombre_ingrediente.strip().capitalize()

        if actual.nombre == objetivo:
            postre.cabeza_ingredientes = actual.siguiente
            actual.siguiente = None
            print(f"[-] Ingrediente '{objetivo}' eliminado (era el primer nodo de '{postre.nombre}').")
            return

        anterior = actual
        actual = actual.siguiente
        while actual is not None:
            if actual.nombre == objetivo:
                anterior.siguiente = actual.siguiente
                actual.siguiente = None
                print(f"[-] Ingrediente '{objetivo}' eliminado de '{postre.nombre}'.")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"[!] Caso verificado: El ingrediente '{objetivo}' no forma parte de '{postre.nombre}'.")

    def alta_postre(self, nombre_postre: str, lista_ingredientes: list[str], permitir_repetidos: bool = False) -> None:
        nombre_limpio = nombre_postre.strip().title()
        if not nombre_limpio:
            print("[!] Caso verificado: El nombre del postre no puede estar vacío.")
            return

        if not permitir_repetidos and self._buscar_indice_postre(nombre_limpio) != -1:
            print(f"[!] Caso verificado: El postre '{nombre_limpio}' ya está dado de alta.")
            return

        nuevo_postre = Postre(nombre_limpio)

        nombres_actuales = [p.nombre for p in self.postres]
        posicion = bisect.bisect_left(nombres_actuales, nombre_limpio)
        self.postres.insert(posicion, nuevo_postre)

        print(f"\n[+] Postre '{nombre_limpio}' insertado en la posición [{posicion}] del arreglo POSTRES.")

        ingredientes_validos = [i.strip() for i in lista_ingredientes if i.strip()]
        if ingredientes_validos:
            ultimo_nodo = None
            vistos = set()
            for ing in ingredientes_validos:
                ing_cap = ing.capitalize()
                if ing_cap.lower() not in vistos:
                    vistos.add(ing_cap.lower())
                    nodo = NodoIngrediente(ing_cap)
                    if nuevo_postre.cabeza_ingredientes is None:
                        nuevo_postre.cabeza_ingredientes = nodo
                    else:
                        ultimo_nodo.siguiente = nodo
                    ultimo_nodo = nodo
            print(f"[+] Se enlazaron {len(vistos)} ingrediente(s) a '{nombre_limpio}'.")
        else:
            print(f"[i] '{nombre_limpio}' se dio de alta sin ingredientes (puntero en NIL).")

    def baja_postre(self, nombre_postre: str) -> None:
        if not self.postres:
            print("[!] Caso verificado: El arreglo POSTRES está vacío; no se puede dar de baja.")
            return

        idx = self._buscar_indice_postre(nombre_postre)
        if idx == -1:
            print(f"[!] Caso verificado: El postre '{nombre_postre}' no existe en el arreglo.")
            return

        postre_eliminado = self.postres[idx]

        actual = postre_eliminado.cabeza_ingredientes
        contador_nodos = 0
        while actual is not None:
            temp = actual.siguiente
            actual.siguiente = None
            actual = temp
            contador_nodos += 1

        postre_eliminado.cabeza_ingredientes = None
        self.postres.pop(idx)
        print(f"[-] Postre '{postre_eliminado.nombre}' y sus {contador_nodos} ingrediente(s) fueron dados de baja.")

    def eliminar_repetidos(self) -> None:
        if len(self.postres) <= 1:
            print("[i] El arreglo tiene 0 o 1 elemento; no existen duplicados por eliminar.")
            return

        print("\n--- Ejecutando limpieza automática de postres repetidos ---")
        i = 0
        eliminados = 0

        while i < len(self.postres) - 1:
            postre_actual = self.postres[i]
            postre_siguiente = self.postres[i + 1]

            if postre_actual.nombre.lower() == postre_siguiente.nombre.lower():
                nodo = postre_siguiente.cabeza_ingredientes
                while nodo is not None:
                    sig = nodo.siguiente
                    nodo.siguiente = None
                    nodo = sig
                postre_siguiente.cabeza_ingredientes = None

                self.postres.pop(i + 1)
                eliminados += 1
                print(f"[-] Duplicado eliminado: '{postre_siguiente.nombre}' en índice [{i + 1}].")
            else:
                self._eliminar_ingredientes_repetidos(postre_actual)
                i += 1

        if self.postres:
            self._eliminar_ingredientes_repetidos(self.postres[-1])

        print(f"[✓] Proceso finalizado. Total de postres duplicados eliminados: {eliminados}.")

    def _eliminar_ingredientes_repetidos(self, postre: Postre) -> None:
        vistos = set()
        actual = postre.cabeza_ingredientes
        anterior = None
        while actual is not None:
            clave = actual.nombre.lower()
            if clave in vistos:
                anterior.siguiente = actual.siguiente
                temp = actual.siguiente
                actual.siguiente = None
                actual = temp
            else:
                vistos.add(clave)
                anterior = actual
                actual = actual.siguiente

    def mostrar_estructura_completa(self) -> None:
        print("\n================ ESTADO DE LA ESTRUCTURA 'POSTRES' ================")
        if not self.postres:
            print("  [Arreglo POSTRES vacío]")
        for idx, p in enumerate(self.postres):
            nodos = []
            curr = p.cabeza_ingredientes
            while curr:
                nodos.append(f"[{curr.nombre}]")
                curr = curr.siguiente
            cadena_nodos = " -> ".join(nodos) + " -> NIL" if nodos else "NIL"
            print(f"  [{idx}] {p.nombre:<18} | --> {cadena_nodos}")
        print("===================================================================\n")


def ejecutar_demo_y_menu():
    gestor = GestorPostres()

    gestor.alta_postre("Flan Napolitano", ["Leche condensada", "Huevo", "Vainilla", "Azúcar"])
    gestor.alta_postre("Gelatina de Limón", [])
    gestor.alta_postre("Arroz con Leche", ["Arroz", "Leche", "Canela", "Pasas"])
    gestor.alta_postre("Pay de Queso", ["Queso crema", "Galleta", "Mantequilla"])
    gestor.alta_postre("Flan Napolitano", ["Leche condensada", "Canela"], permitir_repetidos=True)

    while True:
        gestor.mostrar_estructura_completa()
        print("MENÚ DE OPERACIONES:")
        print("  a) Imprimir lista de ingredientes de un postre")
        print("  b) Insertar nuevos ingredientes a un postre")
        print("  c) Eliminar un ingrediente de un postre")
        print("  d) Dar de alta un postre con sus ingredientes")
        print("  e) Dar de baja un postre con todos sus ingredientes")
        print("  2) [Ejercicio 2] Eliminar automáticamente elementos repetidos")
        print("  s) Salir")

        opcion = input("\nSeleccione una opción: ").strip().lower()

        if opcion == 'a':
            nombre = input("Nombre del postre a consultar: ")
            gestor.imprimir_ingredientes(nombre)
        elif opcion == 'b':
            nombre = input("Nombre del postre: ")
            ing_str = input("Ingrese los nuevos ingredientes separados por coma: ")
            lista_ing = [x.strip() for x in ing_str.split(",") if x.strip()]
            gestor.insertar_ingredientes(nombre, lista_ing)
        elif opcion == 'c':
            nombre = input("Nombre del postre: ")
            ing = input("Nombre del ingrediente a eliminar: ")
            gestor.eliminar_ingrediente(nombre, ing)
        elif opcion == 'd':
            nombre = input("Nombre del nuevo postre: ")
            ing_str = input("Ingredientes separados por coma (dejar en blanco para NIL): ")
            lista_ing = [x.strip() for x in ing_str.split(",") if x.strip()]
            dup = input("¿Permitir duplicado para probar el Ejercicio 2? (s/n): ").strip().lower() == 's'
            gestor.alta_postre(nombre, lista_ing, permitir_repetidos=dup)
        elif opcion == 'e':
            nombre = input("Nombre del postre a dar de baja: ")
            gestor.baja_postre(nombre)
        elif opcion == '2':
            gestor.eliminar_repetidos()
        elif opcion == 's':
            print("Saliendo del programa...")
            break
        else:
            print("[!] Opción no válida.")


if __name__ == "__main__":
    ejecutar_demo_y_menu()