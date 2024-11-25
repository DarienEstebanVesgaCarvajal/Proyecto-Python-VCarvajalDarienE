import os
from modules.mainMenu import displayMenu
from modules.registerExpense import registerExpense
from modules.listExpenses.listAllExpenses import listExpenses
from modules.calculateTotal.calculateTotal import filterExpenses
from modules.generateReports.generateAllReports import generateReports

#Se define la función principal del programa
def main():
    while True:
        #Se muestra el menú principal
        displayMenu()
        try:
            #Se solicita la elección del usuario
            userChoice = int(input("¿Cuál es su elección?: "))
            if userChoice == 1:
                #Se registra un nuevo gasto
                registerExpense()
            elif userChoice == 2:
                #Se listan todos los gastos
                listExpenses()
            elif userChoice == 3:
                #Se calculan los gastos filtrados
                filterExpenses()
            elif userChoice == 4:
                #Se generan reportes de gastos
                generateReports()
            elif userChoice == 5:
                #Se finaliza el programa con un mensaje de despedida
                print("Gracias por usar el simulador. ¡Hasta pronto!")
                break
            else:
                #Se informa al usuario de una selección inválida
                print("Por favor, seleccione una opción válida (1-5).")
        except ValueError:
            #Se maneja la entrada no válida del usuario
            print("Entrada inválida; por favor, ingrese un número del 1 al 5.")
        except KeyboardInterrupt:
            #Se maneja la interrupción por teclado
            print("\nInterrupción detectada; por favor, use la opción 5 para salir.")

#Se inicia el programa si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()