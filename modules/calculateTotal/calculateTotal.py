from modules.utils.fileHandler import readJSON
import os

def calculateTotal():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    title = "Cálculo Total de Gastos"
    instructions = [
        "Calcula el gasto total registrado.",
        "Separa los montos por moneda (COP y USD)."
    ]

    maxLength = max(len(title), *(len(instruction) for instruction in instructions))
    line = ":" * (maxLength + 4)

    os.system('clear')
    print(line)
    print(f"{title:^{maxLength + 4}}")
    print(line)
    for instruction in instructions:
        print(f"{instruction:<{maxLength}}")
    print(line)

    if not expenses["gastos"]:
        print("No hay datos disponibles para calcular los totales.")
        return

    totalCOP = sum(gasto["monto"] for gasto in expenses["gastos"] if gasto["moneda"] == "COP")
    totalUSD = sum(gasto["monto"] for gasto in expenses["gastos"] if gasto["moneda"] == "USD")

    print("Gastos Totales Calculados:")
    print(f"  Total en COP: {totalCOP}")
    print(f"  Total en USD: {totalUSD:.2f}")
    print(line)

    print("¡Cálculo completado exitosamente!")