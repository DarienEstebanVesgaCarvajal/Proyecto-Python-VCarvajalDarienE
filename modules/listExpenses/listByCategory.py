from modules.utils.fileHandler import readJSON
from tabulate import tabulate

def listByCategory():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    if not expenses["gastos"]:
        print("No hay gastos registrados.")
        return

    category = input("Ingrese la categoría que desea consultar: ")

    filteredExpenses = [
        [expense["fecha"], expense["monto"], expense["moneda"], expense["categoría"], expense["descripción"]]
        for expense in expenses["gastos"] if expense["categoría"].lower() == category.lower()
    ]

    if not filteredExpenses:
        print(f"No se encontraron gastos en la categoría '{category}'.")
    else:
        print(f"Gastos en la categoría '{category}':")
        print(tabulate(filteredExpenses, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))