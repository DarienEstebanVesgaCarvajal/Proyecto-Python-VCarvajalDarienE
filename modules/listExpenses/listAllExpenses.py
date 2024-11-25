from modules.utils.fileHandler import readJSON
from tabulate import tabulate

#Se lista y muestra todos los gastos almacenados
def listExpenses():
    #Se define la ruta al archivo de gastos
    filePath = "databases/expenses.json"
    #Se leen los gastos desde el archivo
    expenses = readJSON(filePath)

    #Se verifica si hay gastos para mostrar
    if expenses:
        #Se prepara la tabla con los datos
        table = [[
            expense["date"],
            expense["amount"],
            expense["currency"],
            expense["category"],
            expense["description"]
        ] for expense in expenses]

        #Se imprime la tabla con los gastos
        print(tabulate(table, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))
    else:
        #Se informa al usuario si no hay gastos registrados
        print("No hay gastos registrados para mostrar.")