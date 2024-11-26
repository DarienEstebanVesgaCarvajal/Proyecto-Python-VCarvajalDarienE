# Importa la función displayMenu para mostrar el menú al usuario
from modules.utils.menuDisplay import displayMenu
# Importa las funciones necesarias para listar gastos
from modules.listExpenses.listAllExpenses import listAllExpenses
from modules.listExpenses.listByCategory import listByCategory
from modules.listExpenses.listByDate import listByDate
import os  # Importa el módulo os para realizar operaciones del sistema

# Define la función listExpensesMenu que recibe el parámetro filePath
def listExpensesMenu(filePath):
    os.system('clear')  # Limpia la consola (para sistemas Unix/Linux)

    title = "Listar Gastos"  # Establece un título para el menú
    options = [  # Crea una lista de opciones que el usuario puede seleccionar
        "Ver todos los gastos",
        "Filtrar por categoría",
        "Filtrar por rango de fechas",
        "Regresar al menú principal"
    ]

    # Inicia un bucle infinito para mostrar el menú hasta que el usuario decida salir
    while True:
        # Llama a la función displayMenu para mostrar el título y las opciones al usuario
        displayMenu(title, options)
        # Pide al usuario que seleccione una opción
        choice = input("Seleccione una opción: ").strip()

        # Lógica para manejar la selección del usuario
        if choice == "1":  # Si el usuario selecciona "1"
            listAllExpenses(filePath)  # Llama a la función para listar todos los gastos
        elif choice == "2":  # Si el usuario selecciona "2"
            listByCategory(filePath)  # Llama a la función para filtrar gastos por categoría
        elif choice == "3":  # Si el usuario selecciona "3"
            listByDate(filePath)  # Llama a la función para filtrar gastos por rango de fechas
        elif choice == "4":  # Si el usuario selecciona "4"
            break  # Sale del bucle y regresa al menú principal
        else:  # Si el usuario introduce una opción no válida
            print("Opción inválida. Inténtelo nuevamente.")  # Mensaje que indica la opción es inválida