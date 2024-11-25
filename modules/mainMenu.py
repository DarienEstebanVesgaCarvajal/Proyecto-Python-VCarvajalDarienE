from modules.registerExpense import registerExpense
from modules.listExpenses import listExpenses
from modules.calculateTotal import calculateTotal
from modules.listExpenses.listByCategory import listByCategory
from modules.listExpenses.listByDate import listByDate

def showMainMenu():
    print("\nSeleccione una opción:")
    print("1. Registrar un nuevo gasto")
    print("2. Listar todos los gastos")
    print("3. Calcular total de gastos por moneda")
    print("4. Listar gastos por categoría")
    print("5. Listar gastos por rango de fechas")
    print("6. Salir")

    option = input("Seleccione una opción (1-6): ").strip()

    if option == "1":
        registerExpense()
    elif option == "2":
        listExpenses()
    elif option == "3":
        calculateTotal()
    elif option == "4":
        listByCategory()
    elif option == "5":
        listByDate()
    elif option == "6":
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción no válida. Por favor, intente nuevamente.")