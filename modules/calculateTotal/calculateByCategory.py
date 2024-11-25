from modules.utils.fileHandler import readJSON
from tabulate import tabulate
import os

def calculateByCategory():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    title = "Cálculo Total por Categoría"
    instructions = [
        "Calcula el gasto total agrupado por categoría.",
        "Convierte los montos en USD a COP para unificar los totales."
    ]

    maxLength = max(len(title), *(len(instruction) for instruction in instructions))
    line = ":" * (maxLength + 4)

    os.system('clear')
    print(line)
    print(f"{title:^{maxLength + 4}}")
    print(line)
    for instruction in instructions:
        print(f"{instruction:<{maxLength}}")
    print(line)

    if not expenses["gastos"]:
        print("No hay datos disponibles para calcular por categoría.")
        return

    categories = {}
    for gasto in expenses["gastos"]:
        category = gasto["categoría"]
        amount = gasto["monto"] if gasto["moneda"] == "COP" else gasto["monto"] * 4500
        categories[category] = categories.get(category, 0) + amount

    categoryTable = [[category, amount] for category, amount in categories.items()]
    print("Totales por Categorías (en COP):")
    print(tabulate(categoryTable, headers=["Categoría", "Monto (COP)"], tablefmt="grid"))
    print(line)

    print("¡Cálculo completado exitosamente!")