# Se importa la función para leer datos de archivos JSON
from modules.utils.fileHandler import readJSON
# Se importa os para limpiar la pantalla
import os

# Se calcula el total por categoría
def calculateByCategory():
    filePath = 'databases/expenses.json'  # Ruta al archivo de datos
    expenses = readJSON(filePath)  # Se leen los datos desde el archivo JSON

    # Se establece el título y las instrucciones
    title = "Cálculo Total por Categoría"
    instructions = [
        "Calcula el total agrupado de gastos por categoría.",
        "Los valores están en pesos colombianos (COP)."
    ]

    # Se calcula la longitud máxima para las líneas decorativas
    maxLength = max(len(title), *(len(instruction) for instruction in instructions))
    line = ":" * (maxLength + 4)

    # Se limpia la pantalla y se muestra la cabecera
    os.system('clear')
    print(line)
    print(f"{title:^{maxLength + 4}}")
    print(line)
    for instruction in instructions:
        print(f"{instruction:<{maxLength}}")
    print(line)

    # Se valida si hay gastos para calcular
    if not expenses["gastos"]:
        print("No hay datos disponibles para calcular totales por categoría.")
        return

    # Se agrupan los totales por categoría
    categories = {}
    for expense in expenses["gastos"]:
        category = expense["categoría"]
        amount = expense["monto"] if expense["moneda"] == "COP" else expense["monto"] * 4500
        categories[category] = categories.get(category, 0) + amount

    # Se muestran los totales por categoría
    print("Totales Calculados por Categoría (en COP):")
    for category, total in sorted(categories.items()):
        print(f"  {category}: {total}")
    print(line)

    print("¡Cálculo completado exitosamente!")