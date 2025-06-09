# Lista de estudiantes, cada uno con su nombre y nota
estudiantes = [
    {"nombre": "Ana", "nota": 7},
    {"nombre": "Luis", "nota": 5},
    {"nombre": "Marta", "nota": 9},
    {"nombre": "Carlos", "nota": 6},
    {"nombre": "Julia", "nota": 8}
]

# FUNCION DE ORDENAMIENTO: Burbuja (Bubble Sort)
# Ordena la lista por nota de menor a mayor
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Si la nota actual es mayor que la siguiente, se intercambian
            if lista[j]["nota"] > lista[j + 1]["nota"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# FUNCION DE BÚSQUEDA: Búsqueda lineal
# Busca un estudiante por nombre
def busqueda_lineal(lista, nombre_buscado):
    for estudiante in lista:
        if estudiante["nombre"].lower() == nombre_buscado.lower():
            return estudiante
    return None

# Mostrar la lista original
print("Lista original de estudiantes:")
for est in estudiantes:
    print(f"{est['nombre']} - Nota: {est['nota']}")

# Ordenar la lista y mostrarla
print("\nLista ordenada por nota (de menor a mayor):")
ordenada = ordenar_burbuja(estudiantes.copy())
for est in ordenada:
    print(f"{est['nombre']} - Nota: {est['nota']}")

# Pedir al usuario un nombre para buscar
nombre = input("\n Ingresá el nombre del estudiante a buscar: ")
resultado = busqueda_lineal(estudiantes, nombre)

# Mostrar el resultado de la búsqueda
if resultado:
    print(f"\n Estudiante encontrado: {resultado['nombre']} - Nota: {resultado['nota']}")
else:
    print("\n Estudiante no encontrado.")
