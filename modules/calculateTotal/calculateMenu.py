from modules.utils.menuDisplay import displayMenu
from modules.calculateTotal.calculateByCategory import calculateByCategory
from modules.calculateTotal.calculateByDate import calculateByDate
from modules.calculateTotal.calculateTotal import calculateTotal
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
            calculateByDate(filePath, "diario")
        elif choice == "2":
            calculateByDate(filePath, "semanal")
        elif choice == "3":
            calculateByDate(filePath, "mensual")
        elif choice == "4":
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")