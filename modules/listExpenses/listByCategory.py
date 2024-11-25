from modules.utils.fileHandler import readJSON
from tabulate import tabulate

#Se lista y muestra los gastos filtrados por categoría
def listByCategory():
    #Se solicita al usuario la categoría para filtrar
    category = input("Ingrese la categoría que desea filtrar: ").strip()
    #Se define la ruta al archivo de gastos
    filePath = "databases/expenses.json"
    #Se leen los gastos desde el archivo
    expenses = readJSON(filePath)

    #Se filtran los gastos que coincidan con la categoría
    filteredExpenses = [expense for expense in expenses if expense["category"].lower() == category.lower()]

    #Se verifica si hay gastos para mostrar
    if filteredExpenses:
        #Se prepara la tabla con los datos filtrados
        table = [[
            expense["date"],
            expense["amount"],
            expense["currency"],
            expense["description"]
        ] for expense in filteredExpenses]

        #Se imprime la tabla con los gastos filtrados
        print(tabulate(table, headers=["Fecha", "Monto", "Moneda", "Descripción"], tablefmt="grid"))
    else:
        #Se informa al usuario si no hay gastos registrados para la categoría
        print(f"No hay gastos registrados en la categoría '{category}'.")