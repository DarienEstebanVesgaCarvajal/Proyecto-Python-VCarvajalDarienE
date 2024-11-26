from modules.utils.menuDisplay import displayMenu  # Se importa la función displayMenu para mostrar el menú en pantalla.  
from modules.utils.fileHandler import readJSON  # Se importa la función readJSON para leer archivos JSON.  
from modules.register.registerExpense import registerExpense  # Se importa la función registerExpense para registrar nuevos gastos.  
from modules.listExpenses.listMenu import listExpensesMenu  # Se importa la función listExpensesMenu para listar los gastos registrados.  
from modules.calculateTotal.calculateMenu import calculateTotalMenu  # Se importa la función calculateTotalMenu para calcular totales de gastos.  
from modules.generateReports.generateMenu import generateReportsMenu  # Se importa la función generateReportsMenu para generar reportes de gastos.  
import os  # Se importa el módulo os para interactuar con el sistema operativo (por ejemplo, para limpiar la consola).  

def mainMenu():  
    """  
    Se encarga de mostrar el menú principal del simulador de gastos y manejar la interacción del usuario.  

    Se define la ruta del archivo donde se almacenan los gastos y se gestionan las diferentes opciones del menú.  
    """  
    filePath = 'databases/expenses.json'  # Se especifica la ruta del archivo JSON que contiene los gastos.  
    os.system('clear')  # Se limpia la consola para proporcionar una mejor visualización.  

    title = "Simulador de Gasto Diario"  # Se define el título del menú.  
    options = [  # Se definen las opciones disponibles en el menú.  
        "Registrar nuevo gasto",  
        "Listar gastos",  
        "Calcular total de gastos",  
        "Generar reporte de gastos",  
        "Salir"  
    ]  

    while True:  # Se inicia un bucle para mostrar el menú repetidamente hasta que el usuario decida salir.  
        displayMenu(title, options)  # Se llama a la función para mostrar el menú con el título y las opciones.  
        choice = input("Seleccione una opción: ")  # Se solicita al usuario que seleccione una opción.  

        # Se evalúa la opción seleccionada por el usuario.  
        if choice == "1":  # Si se selecciona la opción para registrar un nuevo gasto.  
            registerExpense(filePath)  # Se llama a la función para registrar un nuevo gasto.  
        elif choice == "2":  # Si se selecciona la opción para listar los gastos.  
            listExpensesMenu(filePath)  # Se llama a la función para mostrar el menú de lista de gastos.  
        elif choice == "3":  # Si se selecciona la opción para calcular el total de gastos.  
            calculateTotalMenu(filePath)  # Se llama a la función para calcular el total de gastos.  
        elif choice == "4":  # Si se selecciona la opción para generar un reporte de gastos.  
            generateReportsMenu(filePath)  # Se llama a la función para mostrar el menú de generación de reportes.  
        elif choice == "5":  # Si se selecciona la opción para salir del programa.  
            print("Saliendo del programa... ¡Hasta luego!")  # Se muestra un mensaje de despedida.  
            break  # Se sale del bucle y finaliza el programa.  
        else:  # Si se proporciona una opción inválida.  
            print("Opción inválida. Inténtelo nuevamente.")  # Se muestra un mensaje indicando que la opción no es válida.