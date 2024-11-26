from modules.calculateTotal.calculateDay import calculateDay
from modules.calculateTotal.calculateWeek import calculateWeek
from modules.calculateTotal.calculateMonth import calculateMonth
from modules.utils.menuDisplay import displayMenu
import os

def calculateTotalMenu(filePath):
    os.system('clear')

    title = "Calcular Total de Gastos"
    options = [
        "Calcular total diario",
        "Calcular total semanal",
        "Calcular total mensual",
        "Regresar al menú principal"
    ]

    while True:
        displayMenu(title, options)
        choice = input("Seleccione una opción: ")

        if choice == "1":
            calculateDay(filePath)
        elif choice == "2":
            calculateWeek(filePath)
        elif choice == "3":
            calculateMonth(filePath)
        elif choice == "4":
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")