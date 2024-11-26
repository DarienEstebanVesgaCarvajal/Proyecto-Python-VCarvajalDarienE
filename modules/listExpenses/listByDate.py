# Se importa la función para leer datos de archivos JSON
from modules.utils.fileHandler import readJSON
# Se importa la librería Tabulate para mostrar los datos en formato tabular
from tabulate import tabulate
# Se importa os para limpiar la pantalla
import os

# Se lista los gastos dentro de un rango de fechas
def listByDate(databasePath):  # Se ajusta el nombre del parámetro
    # Se leen los datos desde el archivo JSON
    expenses = readJSON(databasePath)

    # Valida si la estructura de datos es una lista
    if not isinstance(expenses, list) or not expenses:
        print("El archivo no contiene datos válidos o está vacío.")  # Se muestra un mensaje de error
        return  # Se finaliza la función si la estructura es incorrecta

    # Limpia la pantalla
    os.system('clear')
    print("Lista de Gastos por Rango de Fechas")  # Se imprime el título del listado
    print("Las fechas deben estar en formato DD-MM-AA.")  # Se especifica el formato de fechas

    # Solicita al usuario el rango de fechas
    try:
        startDate = input("Ingrese la fecha de inicio (DD-MM-AA): ").strip()  # Se pide la fecha inicial
        endDate = input("Ingrese la fecha de fin (DD-MM-AA): ").strip()  # Se pide la fecha final
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")  # Maneja la interrupción por teclado
        return

    # Filtra los gastos por rango de fechas
    filteredExpenses = [
        expense for expense in expenses
        if startDate <= expense["fecha"] <= endDate  # Compara las fechas ingresadas con las del archivo
    ]

    # Valida si hay resultados
    if not filteredExpenses:
        print(f"No se encontraron gastos entre '{startDate}' y '{endDate}'.")  # Muestra un mensaje si no hay resultados
        return  # Se finaliza la función si no hay gastos en el rango

    # Prepara los datos en una tabla
    table = [
        [
            expense.get("fecha", "N/A"),
            expense.get("nombre", "N/A"),
            expense.get("categoria", expense.get("categoría", "N/A")),  # Maneja ambas claves
            expense.get("monto", "N/A"),
        ]
        for expense in filteredExpenses  # Se recorre la lista filtrada para obtener los datos
    ]

    # Se imprime la tabla en formato tabular
    print(tabulate(table, headers=["Fecha", "Nombre", "Categoría", "Monto"], tablefmt="grid"))
    print("\n¡Listado por rango de fechas completado exitosamente!")  # Se confirma el listado completado