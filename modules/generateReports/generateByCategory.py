from modules.utils.fileHandler import readJSON
from tabulate import tabulate
import os

def generateByCategory():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    title = "Reporte de Gastos por Categoría"
    instructions = [
        "Este reporte muestra el detalle total por categoría.",
        "Incluye todos los gastos agrupados y ordenados alfabéticamente."
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
        print("No hay datos disponibles para generar un reporte.")
        return

    categories = {}
    for gasto in expenses["gastos"]:
        category = gasto["categoría"]
        amount = gasto["monto"] if gasto["moneda"] == "COP" else gasto["monto"] * 4500
        categories[category] = categories.get(category, 0) + amount

    categoryTable = [[category, amount] for category, amount in sorted(categories.items())]
    print("Detalle por Categorías (en COP):")
    print(tabulate(categoryTable, headers=["Categoría", "Monto (COP)"], tablefmt="grid"))
    print(line)

    print("¡Reporte generado exitosamente!")