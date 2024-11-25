from modules.utils.fileHandler import readJSON
from tabulate import tabulate
import os

def generateAllReports():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    # Título del reporte
    title = "Reporte Completo de Gastos"

    # Instrucciones del reporte
    instructions = [
        "Este reporte incluye:",
        "- Resumen de gastos totales (COP y USD).",
        "- Detalle de gastos por categoría.",
        "- Lista completa de gastos registrados."
    ]

    # Cálculo del ancho máximo para la línea decorativa
    maxLength = max(len(title), *(len(instruction) for instruction in instructions))
    line = ":" * (maxLength + 4)  # Línea decorativa ajustada al máximo

    # Limpia la consola y muestra el encabezado
    os.system('clear')
    print(line)
    print(f"{title:^{maxLength + 4}}")  # Centra el título
    print(line)
    for instruction in instructions:
        print(f"{instruction:<{maxLength}}")  # Ajusta las instrucciones al ancho máximo
    print(line)

    # Verifica si hay datos disponibles
    if not expenses["gastos"]:
        print("No hay datos disponibles para generar un reporte.")
        return

    # Resumen de gastos totales
    totalCOP = sum(gasto["monto"] for gasto in expenses["gastos"] if gasto["moneda"] == "COP")
    totalUSD = sum(gasto["monto"] for gasto in expenses["gastos"] if gasto["moneda"] == "USD")

    print("Resumen de Gastos Totales:")
    print(f"  Total en COP: {totalCOP}")
    print(f"  Total en USD: {totalUSD:.2f}")
    print(line)

    # Resumen por categorías (en COP)
    categories = {}
    for gasto in expenses["gastos"]:
        category = gasto["categoría"]
        amount = gasto["monto"] if gasto["moneda"] == "COP" else gasto["monto"] * 4500  # Conversión USD a COP
        categories[category] = categories.get(category, 0) + amount

    categoryTable = [[category, amount] for category, amount in categories.items()]
    print("Resumen por Categorías (en COP):")
    print(tabulate(categoryTable, headers=["Categoría", "Monto (COP)"], tablefmt="grid"))
    print(line)

    # Lista completa de gastos
    fullTable = [
        [gasto["fecha"], gasto["monto"], gasto["moneda"], gasto["categoría"], gasto["descripción"]]
        for gasto in expenses["gastos"]
    ]
    print("Lista Completa de Gastos:")
    print(tabulate(fullTable, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))
    print(line)

    print("¡Reporte generado exitosamente!")