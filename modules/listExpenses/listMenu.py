from modules.utils.menuDisplay import displayMenu
from modules.listExpenses.listAllExpenses import listAllExpenses
from modules.listExpenses.listByCategory import listByCategory
from modules.listExpenses.listByDate import listByDate
import os

def listExpensesMenu(filePath):
    os.system('clear')

    title = "Listar Gastos"
    options = [
        "Ver todos los gastos",
        "Filtrar por categoría",
        "Filtrar por rango de fechas",
        "Regresar al menú principal"
    ]

    while True:
        displayMenu(title, options)
        choice = input("Seleccione una opción: ")

        if choice == "1":
            listAllExpenses(filePath)
        elif choice == "2":
            listByCategory(filePath)
        elif choice == "3":
            listByDate(filePath)
        elif choice == "4":
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")