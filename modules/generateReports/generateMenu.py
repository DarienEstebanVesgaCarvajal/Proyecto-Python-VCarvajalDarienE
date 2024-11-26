from modules.utils.menuDisplay import displayMenu
from modules.generateReports.generateAllReports import generateAllReports
from modules.generateReports.generateByCategory import generateByCategory
from modules.generateReports.generateByDate import generateByDate
import os

def generateReportsMenu(filePath):
    os.system('clear')

    title = "Generar Reporte de Gastos"
    options = [
        "Reporte diario",
        "Reporte semanal",
        "Reporte mensual",
        "Regresar al menú principal"
    ]

    while True:
        displayMenu(title, options)
        choice = input("Seleccione una opción: ")

        if choice == "1":
            generateByDate(filePath, "diario")
        elif choice == "2":
            generateByDate(filePath, "semanal")
        elif choice == "3":
            generateByDate(filePath, "mensual")
        elif choice == "4":
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")