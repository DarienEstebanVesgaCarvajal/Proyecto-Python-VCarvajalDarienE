from modules.utils.fileHandler import readJSON
from tabulate import tabulate
from datetime import datetime

#Se lista y muestra los gastos dentro de un rango de fechas
def listByDate():
    #Se solicita al usuario las fechas inicial y final
    startDate = input("Ingrese la fecha inicial (DD-MM-AA): ").strip()
    endDate = input("Ingrese la fecha final (DD-MM-AA): ").strip()
    #Se define la ruta al archivo de gastos
    filePath = "databases/expenses.json"
    #Se leen los gastos desde el archivo
    expenses = readJSON(filePath)

    try:
        #Se convierte el rango de fechas a objetos de tipo datetime
        start = datetime.strptime(startDate, "%d-%m-%y")
        end = datetime.strptime(endDate, "%d-%m-%y")

        #Se filtran los gastos dentro del rango de fechas
        filteredExpenses = [
            expense for expense in expenses
            if start <= datetime.strptime(expense["date"], "%d-%m-%y") <= end
        ]

        #Se verifica si hay gastos para mostrar
        if filteredExpenses:
            #Se prepara la tabla con los datos filtrados
            table = [[
                expense["date"],
                expense["amount"],
                expense["currency"],
                expense["category"],
                expense["description"]
            ] for expense in filteredExpenses]

            #Se imprime la tabla con los gastos filtrados
            print(tabulate(table, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))
        else:
            #Se informa al usuario si no hay gastos registrados en el rango
            print("No hay gastos registrados en el rango de fechas especificado.")
    except ValueError:
        #Se informa al usuario si las fechas ingresadas son inválidas
        print("Por favor, ingrese fechas válidas en el formato DD-MM-AA.")