# Se importa la librería json para trabajar con archivos JSON  
import json  
# Se importa la librería tabulate para mostrar datos en formato tabular  
from tabulate import tabulate  

# Se define la función listAllExpenses que recibe la ruta del archivo como parámetro  
def listAllExpenses(filePath):  
    try:  
        # Se intenta abrir el archivo en modo lectura  
        with open(filePath, 'r') as file:  
            expenses = json.load(file)  # Carga el archivo JSON y lo convierte en una lista de diccionarios  
        
        # Verifica si la lista de gastos está vacía  
        if not expenses:  
            print("No hay gastos registrados.")  # Mensaje si no se han registrado gastos  
            return  # Sale de la función si no hay gastos  

        # Crea la tabla: cada fila contiene los datos de un gasto  
        table = [[expense["fecha"], expense["monto"], expense["categoria"], expense.get("descripcion", "N/A")]  
                 for expense in expenses]  # Utiliza una lista por comprensión para formar la tabla  
        
        # Establece los encabezados de la tabla  
        headers = ["Fecha", "Monto", "Categoría", "Descripción"]  
        print(tabulate(table, headers, tablefmt="grid"))  # Imprime la tabla en formato de cuadrícula  

    # Manejo de excepciones  
    except FileNotFoundError:  
        print("No se encontró el archivo de gastos.")  # Mensaje si el archivo no existe  
    except json.JSONDecodeError:  
        print("El archivo de datos está corrupto o vacío.")  # Mensaje si el archivo no es un JSON válido  
    except KeyError as e:  
        print(f"Falta la clave esperada: {e}")  # Mensaje si falta una clave en el diccionario  

# Se importa la función para leer datos de archivos JSON  
from modules.utils.fileHandler import readJSON  
# Se importa la librería Tabulate para mostrar los datos en formato tabular  
from tabulate import tabulate  
# Se define la función listAllExpenses que recibe la ruta de la base de datos como parámetro  
def listAllExpenses(databasePath):  
    try:  
        # Se leen los datos existentes del archivo JSON utilizando la función readJSON  
        existingData = readJSON(databasePath)  
        
        # Se verifica si no hay gastos registrados  
        if not existingData:  
            print("No hay gastos registrados.")  # Se imprime un mensaje cuando no se encuentran gastos  
            return  # Se sale de la función si no hay datos  

        # Se crea una tabla con los datos de los gastos  
        table = [  
            [  
                expense["fecha"],  # Se extrae la fecha del gasto  
                expense["monto"],  # Se extrae el monto del gasto  
                expense.get("categoria", "Sin categoría"),  # Se obtiene la categoría del gasto; se usa "Sin categoría" si no se especifica  
                expense["nombre"]  # Se extrae el nombre asociado al gasto  
            ]  
            for expense in existingData  # Se recorre cada gasto en los datos existentes  
        ]  
        
        # Se muestra la tabla usando tabulate  
        print("\nGastos registrados:")  # Se imprime un mensaje antes de mostrar la tabla  
        print(tabulate(table, headers=["Fecha", "Monto", "Categoría", "Nombre"], tablefmt="grid"))  # Se imprime la tabla en formato de cuadrícula  
    except Exception as e:  
        # Se captura cualquier excepción que ocurra y se muestra un mensaje de error  
        print(f"Ocurrió un error al listar los gastos: {e}")  # Se imprime un mensaje de error con información sobre la excepción