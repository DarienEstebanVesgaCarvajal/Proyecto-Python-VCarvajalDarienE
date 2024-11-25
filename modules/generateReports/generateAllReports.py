from modules.utils.fileHandler import readJSON
from tabulate import tabulate
import os

def generateAllReports():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    title = "Reporte Completo de Gastos"
    instructions = [
        "Este reporte incluye:",
        "- Resumen de gastos totales (COP y USD).",
        "- Detalle de gastos por categoría.",
        "- Lista completa de gastos registrados."
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

    totalCOP = sum(gasto["monto"] for gasto in expenses["gastos"] if gasto["moneda"] == "COP")
    totalUSD = sum(gasto["monto"] for gasto in expenses["gastos"] if gasto["moneda"] == "USD")

    print("Resumen de Gastos Totales:")
    print(f"  Total en COP: {totalCOP}")
    print(f"  Total en USD: {totalUSD:.2f}")
    print(line)

    categories = {}
    for gasto in expenses["gastos"]:
        category = gasto["categoría"]
        amount = gasto["monto"] if gasto["moneda"] == "COP" else gasto["monto"] * 4500  # Suponiendo USD = 4500 COP
        categories[category] = categories.get(category, 0) + amount

    categoryTable = [[category, amount] for category, amount in categories.items()]
    print("Resumen por Categorías (en COP):")
    print(tabulate(categoryTable, headers=["Categoría", "Monto (COP)"], tablefmt="grid"))
    print(line)

    fullTable = [
        [gasto["fecha"], gasto["monto"], gasto["moneda"], gasto["categoría"], gasto["descripción"]]
        for gasto in expenses["gastos"]
    ]
    print("Lista Completa de Gastos:")
    print(tabulate(fullTable, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))
    print(line)

    print("¡Reporte generado exitosamente!")