from modules.utils.menuDisplay import displayMenu
from modules.utils.fileHandler import readJSON
from modules.register.registerExpense import registerExpense
from modules.listExpenses.listMenu import listExpensesMenu
from modules.calculateTotal.calculateMenu import calculateTotalMenu
from modules.generateReports.generateMenu import generateReportsMenu
import os

def mainMenu():
    filePath = 'databases/expenses.json'
    os.system('clear')

    title = "Simulador de Gasto Diario"
    options = [
        "Registrar nuevo gasto",
        "Listar gastos",
        "Calcular total de gastos",
        "Generar reporte de gastos",
        "Salir"
    ]

    while True:
        displayMenu(title, options)
        choice = input("Seleccione una opción: ")

        if choice == "1":
            registerExpense(filePath)
        elif choice == "2":
            listExpensesMenu(filePath)
        elif choice == "3":
            calculateTotalMenu(filePath)
        elif choice == "4":
            generateReportsMenu(filePath)
        elif choice == "5":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")