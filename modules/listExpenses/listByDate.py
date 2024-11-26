# Se importa la función para leer datos de archivos JSON
from modules.utils.fileHandler import readJSON
# Se importa la librería Tabulate para mostrar los datos en formato tabular
from tabulate import tabulate
# Se importa os para limpiar la pantalla
import os

# Se lista los gastos dentro de un rango de fechas
def listByDate():
    filePath = 'databases/expenses.json'  # Ruta al archivo de datos
    expenses = readJSON(filePath)  # Se leen los datos desde el archivo JSON

    # Se establece el título y las instrucciones
    title = "Lista de Gastos por Rango de Fechas"
    instructions = [
        "Seleccione un rango de fechas para filtrar los gastos.",
        "Las fechas deben estar en formato DD-MM-AA."
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

    # Se solicitan las fechas al usuario
    startDate = input("Ingrese la fecha de inicio (DD-MM-AA): ").strip()
    endDate = input("Ingrese la fecha de fin (DD-MM-AA): ").strip()

    # Se filtran los gastos por el rango de fechas
    filteredExpenses = [
        expense for expense in expenses["gastos"]
        if startDate <= expense["fecha"] <= endDate
    ]

    # Se valida si hay gastos en el rango de fechas
    if not filteredExpenses:
        print(f"No se encontraron gastos entre '{startDate}' y '{endDate}'.")
        return

    # Se prepara la tabla para mostrar los gastos filtrados
    table = [
        [expense["fecha"], expense["monto"], expense["moneda"], expense["categoría"], expense["descripción"]]
        for expense in filteredExpenses
    ]

    # Se imprime la tabla
    print(tabulate(table, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))
    print(line)

    print("¡Listado por rango de fechas completado exitosamente!")