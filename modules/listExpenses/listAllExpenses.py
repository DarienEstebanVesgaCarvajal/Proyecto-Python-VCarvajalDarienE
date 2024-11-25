from modules.utils.fileHandler import readJSON
from tabulate import tabulate

def listExpenses():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    if not expenses["gastos"]:
        print("No hay gastos registrados.")
        return

    tableData = [
        [expense["fecha"], expense["monto"], expense["moneda"], expense["categoría"], expense["descripción"]]
        for expense in expenses["gastos"]
    ]

    print("Lista Completa de Gastos:")
    print(tabulate(tableData, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))