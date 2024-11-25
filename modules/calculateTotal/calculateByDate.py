from modules.utils.fileHandler import readJSON
from tabulate import tabulate
import os

def calculateByDate():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    title = "Cálculo Total por Fecha"
    instructions = [
        "Calcula el gasto total agrupado por fecha.",
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
        print("No hay datos disponibles para calcular por fecha.")
        return

    dates = {}
    for gasto in expenses["gastos"]:
        date = gasto["fecha"]
        amount = gasto["monto"] if gasto["moneda"] == "COP" else gasto["monto"] * 4500
        dates[date] = dates.get(date, 0) + amount

    dateTable = [[date, amount] for date, amount in sorted(dates.items())]
    print("Totales por Fechas (en COP):")
    print(tabulate(dateTable, headers=["Fecha", "Monto (COP)"], tablefmt="grid"))
    print(line)

    print("¡Cálculo completado exitosamente!")