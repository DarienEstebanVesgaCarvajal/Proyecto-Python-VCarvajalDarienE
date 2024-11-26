import json
# Se importa la librería tabulate para mostrar datos en formato tabular
from tabulate import tabulate
# Se importa la función para leer archivos JSON
from modules.utils.fileHandler import readJSON

# Se define la función listByCategory que recibe la ruta del archivo como parámetro
def listByCategory(filePath):
    try:
        # Se leen los datos desde el archivo JSON
        expenses = readJSON(filePath)  

        # Verifica si la lista de gastos está vacía o no contiene claves esperadas
        if not expenses:
            print("No hay gastos registrados.")  # Mensaje si no hay datos
            return
        
        # Se obtienen las categorías únicas de los gastos, manejando claves faltantes
        categories = set(
            expense.get("categoria", "Sin categoría") for expense in expenses
        )
        print("\nCategorías disponibles:")  # Se imprime un mensaje antes de listar las categorías
        for category in categories:
            print(f"- {category}")  # Lista cada categoría encontrada
        
        # Solicita al usuario una categoría
        selectedCategory = input("Ingrese la categoría que desea filtrar: ").strip()

        # Filtra los gastos por la categoría seleccionada
        filteredExpenses = [
            expense for expense in expenses if expense.get("categoria", "Sin categoría") == selectedCategory
        ]

        # Verifica si hay gastos en la categoría seleccionada
        if not filteredExpenses:
            print(f"\nNo se encontraron gastos en la categoría '{selectedCategory}'.")  # Mensaje si no hay coincidencias
            return

        # Prepara e imprime los datos en una tabla
        table = [
            [
                expense["fecha"],  # Extrae la fecha del gasto
                expense["monto"],  # Extrae el monto del gasto
                expense.get("descripcion", "N/A")  # Extrae la descripción; usa "N/A" si no está especificada
            ]
            for expense in filteredExpenses
        ]
        # Se imprime la tabla con encabezados claros
        print(tabulate(table, headers=["Fecha", "Monto", "Descripción"], tablefmt="grid"))
        print(f"\n¡Listado de gastos en la categoría '{selectedCategory}' completado!")  # Mensaje de finalización

    except FileNotFoundError:
        print("No se encontró el archivo de gastos.")  # Mensaje si el archivo no existe
    except json.JSONDecodeError:
        print("El archivo de datos está corrupto o vacío.")  # Mensaje si el archivo no es válido
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")  # Manejo de cualquier otro error