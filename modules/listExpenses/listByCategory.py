# Se importa la función para leer datos de archivos JSON
from modules.utils.fileHandler import readJSON
# Se importa la librería Tabulate para mostrar los datos en formato tabular
from tabulate import tabulate
# Se importa os para limpiar la pantalla
import os

# Se lista los gastos agrupados por categoría
def listByCategory():
    filePath = 'databases/expenses.json'  # Ruta al archivo de datos
    expenses = readJSON(filePath)  # Se leen los datos desde el archivo JSON

    # Se establece el título y las instrucciones
    title = "Lista de Gastos por Categoría"
    instructions = [
        "Seleccione una categoría para filtrar los gastos.",
        "Se mostrará una lista detallada con fecha, monto, moneda y descripción."
    ]

    # Se calcula la longitud máxima para las líneas decorativas
    maxLength = max(len(title), *(len(instruction) for instruction in instructions))
    line = ":" * (maxLength + 4)

    # Se limpia la pantalla y se muestra la cabecera
    os.system('clear')
    print(line)
    print(f"{title:^{maxLength + 4}}")
    print(line)
    for instruction in instructions:
        print(f"{instruction:<{maxLength}}")
    print(line)

    # Se solicita la categoría al usuario
    category = input("Ingrese la categoría para filtrar: ").strip()

    # Se filtran los gastos por la categoría seleccionada
    filteredExpenses = [
        expense for expense in expenses["gastos"] if expense["categoría"].lower() == category.lower()
    ]

    # Se valida si hay gastos en la categoría
    if not filteredExpenses:
        print(f"No se encontraron gastos en la categoría '{category}'.")
        return

    # Se prepara la tabla para mostrar los gastos filtrados
    table = [
        [expense["fecha"], expense["monto"], expense["moneda"], expense["descripción"]]
        for expense in filteredExpenses
    ]

    # Se imprime la tabla
    print(tabulate(table, headers=["Fecha", "Monto", "Moneda", "Descripción"], tablefmt="grid"))
    print(line)

    print("¡Listado por categoría completado exitosamente!")