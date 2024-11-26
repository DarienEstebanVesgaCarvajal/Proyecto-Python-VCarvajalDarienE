# Se importan las funciones para generar reportes diarios, semanales y mensuales  
from modules.generateReports.generateDay import generateDay  
from modules.generateReports.generateWeek import generateWeek  
from modules.generateReports.generateMonth import generateMonth  

# Se define la función para mostrar el menú de generación de reportes  
def generateReportsMenu(filePath):  
    import os  # Se importa el módulo os para realizar operaciones del sistema  
    os.system('clear')  # Se limpia la pantalla de la consola  

    title = "Generar Reporte de Gastos"  # Título del menú  
    options = [  # Opciones del menú  
        "Reporte diario",  
        "Reporte semanal",  
        "Reporte mensual",  
        "Regresar al menú principal"  
    ]  

    while True:  # Bucle de menú que se ejecuta indefinidamente hasta que el usuario elige salir  
        # Se imprime el título y las líneas decorativas  
        print("\n" + ":" * 40)  # Línea decorativa superior  
        print(f"{title:^40}")  # Centra el título en 40 espacios  
        print(":" * 40)  # Línea decorativa inferior  

        # Se imprimen las opciones del menú numeradas  
        for idx, option in enumerate(options, start=1):  
            print(f"{idx}. {option}")  # Imprime cada opción con su índice  
        print(":" * 40)  # Línea decorativa final  

        choice = input("Seleccione una opción: ")  # Se solicita al usuario que elija una opción  

        # Se verifica la opción seleccionada por el usuario  
        if choice == "1":  # Para el reporte diario  
            generateDay(filePath)  # Llama a la función para generar el reporte diario  
        elif choice == "2":  # Para el reporte semanal  
            generateWeek(filePath)  # Llama a la función para generar el reporte semanal  
        elif choice == "3":  # Para el reporte mensual  
            generateMonth(filePath)  # Llama a la función para generar el reporte mensual  
        elif choice == "4":  # Para regresar al menú principal  
            break  # Sale del bucle y finaliza el menú  
        else:  # Si la opción no es válida  
            print("Opción inválida. Inténtelo nuevamente.")  # Mensaje de error para opción no válida