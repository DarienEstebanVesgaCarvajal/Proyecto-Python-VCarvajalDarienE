import os
from modules.mainMenu import displayMenu
from modules.registerExpense import registerExpense
from modules.listExpenses.listAllExpenses import listExpenses
from modules.calculateTotal.calculateTotal import filterExpenses
from modules.generateReports.generateAllReports import generateReports

def main():
    while True:
        displayMenu()
        try:
            userChoice = int(input("¿Cuál es su elección?: "))
            if userChoice == 1:
                registerExpense()
            elif userChoice == 2:
                listExpenses()
            elif userChoice == 3:
                filterExpenses()
            elif userChoice == 4:
                generateReports()
            elif userChoice == 5:
                print("Gracias por usar el simulador. ¡Hasta pronto!")
                break
            else:
                print("Por favor, seleccione una opción válida (1-5).")
        except ValueError:
            print("Entrada inválida; por favor, ingrese un número del 1 al 5.")
        except KeyboardInterrupt:
            print("\nInterrupción detectada; por favor, use la opción 5 para salir.")

if __name__ == "__main__":
    main()