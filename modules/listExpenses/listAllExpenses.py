# Se importa la función para leer datos de archivos JSON
from modules.utils.fileHandler import readJSON
# Se importa la librería Tabulate para mostrar los datos en formato tabular
from tabulate import tabulate
# Se importa os para limpiar la pantalla
import os

# Se lista todos los gastos registrados
def listAllExpenses():
    filePath = 'databases/expenses.json'  # Ruta al archivo de datos
    expenses = readJSON(filePath)  # Se leen los datos desde el archivo JSON

    # Se establece el título y las instrucciones
    title = "Lista Completa de Gastos"
    instructions = [
        "Este listado incluye todos los gastos registrados.",
        "Cada gasto se muestra con fecha, monto, moneda, categoría y descripción."
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

    # Se valida si hay gastos para mostrar
    if not expenses["gastos"]:
        print("No hay datos disponibles para mostrar.")
        return

    # Se prepara la tabla para mostrar los gastos
    table = [
        [expense["fecha"], expense["monto"], expense["moneda"], expense["categoría"], expense["descripción"]]
        for expense in expenses["gastos"]
    ]

    # Se imprime la tabla
    print(tabulate(table, headers=["Fecha", "Monto", "Moneda", "Categoría", "Descripción"], tablefmt="grid"))
    print(line)

    print("¡Listado completado exitosamente!")