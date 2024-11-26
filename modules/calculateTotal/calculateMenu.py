from modules.calculateTotal.calculateDay import calculateDay  # Se importa la función calculateDay para calcular gastos diarios.  
from modules.calculateTotal.calculateWeek import calculateWeek  # Se importa la función calculateWeek para calcular gastos semanales.  
from modules.calculateTotal.calculateMonth import calculateMonth  # Se importa la función calculateMonth para calcular gastos mensuales.  
from modules.utils.menuDisplay import displayMenu  # Se importa la función displayMenu para mostrar el menú en pantalla.  
import os  # Se importa el módulo os para limpiar la consola.  

def calculateTotalMenu(filePath):  
    """  
    Se encarga de mostrar el menú para calcular totales de gastos y ejecutar la opción seleccionada.  

    :param filePath: Se especifica la ruta del archivo que contiene los gastos.  
    """  
    os.system('clear')  # Se limpia la consola para proporcionar una mejor visualización.  

    title = "Calcular Total de Gastos"  # Se define el título del menú.  
    options = [  # Se definen las opciones disponibles en el menú.  
        "Calcular total diario",  
        "Calcular total semanal",  
        "Calcular total mensual",  
        "Regresar al menú principal"  
    ]  

    while True:  # Se inicia un bucle para mostrar el menú repetidamente hasta que el usuario decida salir.  
        displayMenu(title, options)  # Se llama a la función para mostrar el menú con el título y las opciones.  
        choice = input("Seleccione una opción: ")  # Se solicita al usuario que seleccione una opción.  

        # Se evalúa la opción seleccionada por el usuario.  
        if choice == "1":  # Si se selecciona la opción para calcular el total diario.  
            calculateDay(filePath)  # Se llama a la función para calcular el total diario.  
        elif choice == "2":  # Si se selecciona la opción para calcular el total semanal.  
            calculateWeek(filePath)  # Se llama a la función para calcular el total semanal.  
        elif choice == "3":  # Si se selecciona la opción para calcular el total mensual.  
            calculateMonth(filePath)  # Se llama a la función para calcular el total mensual.  
        elif choice == "4":  # Si se selecciona la opción para regresar al menú principal.  
            break  # Se sale del bucle y retorna al menú principal.  
        else:  # Si se proporciona una opción inválida.  
            print("Opción inválida. Inténtelo nuevamente.")  # Se muestra un mensaje indicando que la opción no es válida.