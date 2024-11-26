from modules.registerExpense import registerExpense
from modules.listExpenses import listExpenses
from modules.calculateTotal import calculateTotal
from modules.listExpenses.listByCategory import listByCategory
from modules.listExpenses.listByDate import listByDate

#Se muestra el menú principal al usuario
def displayMenu():
    #Se imprime el menú con las opciones disponibles
    print("\nSeleccione una opción:")
    print("1. Registrar un nuevo gasto")
    print("2. Listar todos los gastos")
    print("3. Calcular total de gastos por moneda")
    print("4. Listar gastos por categoría")
    print("5. Listar gastos por rango de fechas")
    print("6. Salir")

    #Se solicita la opción al usuario
    option = input("Seleccione una opción (1-6): ").strip()

    #Se evalúa la opción ingresada
    if option == "1":
        #Se llama a la función para registrar un gasto
        registerExpense()
    elif option == "2":
        #Se llama a la función para listar todos los gastos
        listExpenses()
    elif option == "3":
        #Se llama a la función para calcular el total de gastos
        calculateTotal()
    elif option == "4":
        #Se llama a la función para listar los gastos por categoría
        listByCategory()
    elif option == "5":
        #Se llama a la función para listar los gastos por rango de fechas
        listByDate()
    elif option == "6":
        #Se imprime un mensaje de despedida y se cierra el programa
        print("Saliendo del programa...")
        exit()
    else:
        #Se notifica al usuario sobre una opción no válida
        print("Opción no válida. Por favor, intente nuevamente.")