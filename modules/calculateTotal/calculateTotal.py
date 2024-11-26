# Se importa la función para leer datos de archivos JSON
from modules.utils.fileHandler import readJSON
# Se importa os para limpiar la pantalla
import os

# Se calcula el total general de gastos
def calculateTotal():
    filePath = 'databases/expenses.json'  # Ruta al archivo de datos
    expenses = readJSON(filePath)  # Se leen los datos desde el archivo JSON

    # Se establece el título y las instrucciones
    title = "Cálculo Total de Gastos"
    instructions = [
        "Calcula el gasto total registrado.",
        "Separa los montos por moneda (COP y USD)."
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

    # Se valida si hay gastos para calcular el total
    if not expenses["gastos"]:
        print("No hay datos disponibles para calcular los totales.")
        return

    # Se calculan los totales por moneda
    totalCOP = sum(expense["monto"] for expense in expenses["gastos"] if expense["moneda"] == "COP")
    totalUSD = sum(expense["monto"] for expense in expenses["gastos"] if expense["moneda"] == "USD")

    # Se muestran los totales calculados
    print("Gastos Totales Calculados:")
    print(f"  Total en COP: {totalCOP}")
    print(f"  Total en USD: {totalUSD:.2f}")
    print(line)

    print("¡Cálculo completado exitosamente!")