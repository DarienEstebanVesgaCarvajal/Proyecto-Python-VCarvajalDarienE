import os

def displayMenu():
    title = "Simulador de Gastos"
    options = [
        "Seleccione una opción:",
        "1. Registrar nuevo gasto",
        "2. Listar gastos",
        "3. Calcular total de gastos",
        "4. Generar reporte de gastos",
        "5. Salir"
    ]

    maxLength = max(len(title), *(len(option) for option in options))
    line = (":" * (maxLength + 4))

    os.system('clear')
    print(line)
    print(f"{title:^{maxLength + 4}}")
    print(line)
    for option in options:
        print(f"{option:<{maxLength}}")
    print(line)