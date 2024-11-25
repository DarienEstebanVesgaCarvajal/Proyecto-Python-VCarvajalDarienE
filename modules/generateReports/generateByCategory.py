from modules.utils.fileHandler import readJSON
from tabulate import tabulate

def generateByCategory():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    if not expenses["gastos"]:
        print("No hay gastos registrados.")
        return

    categories = {}
    for expense in expenses["gastos"]:
        category = expense["categoría"]
        amount = expense["monto"] if expense["moneda"] == "COP" else expense["monto"] * 4500
        categories[category] = categories.get(category, 0) + amount

    categoryTable = [[category, amount] for category, amount in categories.items()]

    print("Reporte por Categorías:")
    print(tabulate(categoryTable, headers=["Categoría", "Monto (COP)"], tablefmt="grid"))