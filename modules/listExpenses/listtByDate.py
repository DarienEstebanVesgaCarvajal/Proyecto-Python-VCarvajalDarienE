from modules.utils.fileHandler import readJSON
from tabulate import tabulate

def listByDate():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    if not expenses["gastos"]:
        print("No hay gastos registrados.")
        return

    startDate = input("Ingrese la fecha de inicio (DD-MM-AA): ")
    endDate = input("Ingrese la fecha de fin (DD-MM-AA): ")

    filteredExpenses = [
        [expense["fecha"], expense["monto"], expense["moneda"], expense["categoría"], expense["descripción"]]
        for expense in expenses["gastos"]
        if startDate <= expense["fecha"] <= endDate
    ]

    if not filteredExpenses:
        print(f"No se encontraron gastos entre {startDate} y {endDate}.")
    else:
        print(f"Gastos entre {startDate} y {endDate}:")
        print(tabulate(filteredExpenses, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))