# Se importa la función para leer datos de archivos JSON
from modules.utils.fileHandler import readJSON
# Se importa Tabulate para el formato de tablas
from tabulate import tabulate
# Se importa os para limpiar la pantalla
import os

# Se genera un reporte agrupado por fechas
def generateByDate():
    filePath = 'databases/expenses.json'  # Ruta al archivo de datos
    expenses = readJSON(filePath)  # Se leen los datos desde el archivo JSON

    # Se establece el título y las instrucciones
    title = "Reporte de Gastos por Fecha"
    instructions = [
        "Este reporte organiza todos los gastos por orden cronológico.",
        "Incluye totales diarios para facilitar el análisis."
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

    # Se valida si hay gastos para generar el reporte
    if not expenses["gastos"]:
        print("No hay datos disponibles para generar un reporte.")
        return

    # Se procesan los datos agrupados por fecha
    dates = {}
    for expense in expenses["gastos"]:
        date = expense["fecha"]
        amount = expense["monto"] if expense["moneda"] == "COP" else expense["monto"] * 4500
        dates[date] = dates.get(date, 0) + amount

    # Se prepara la tabla con los datos agrupados
    dateTable = [[date, amount] for date, amount in sorted(dates.items())]
    print("Detalle por Fechas (en COP):")
    print(tabulate(dateTable, headers=["Fecha", "Monto (COP)"], tablefmt="grid"))
    print(line)

    print("¡Reporte generado exitosamente!")