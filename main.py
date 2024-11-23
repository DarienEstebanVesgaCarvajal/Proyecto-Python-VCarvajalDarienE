import os
# from modules import registerExpense
# from modules import listExpenses
# from modules import calculateTotal
# from modules import generateReport

def displayMenu():
    title = "Simulador de Gasto Diario"
    options = [
        "Seleccione una opción:",
        "1. Registrar nuevo gasto",
        "2. Listar gastos",
        "3. Calcular total de gastos",
        "4. Generar reporte de gastos",
        "5. Salir"
    ]

    maxLength = max(len(title), *(len(option) for option in options))
    line = ("=" * (maxLength + 4))

    os.system('clear')
    print(line)
    print(f"{title:^{maxLength + 4}}")
    print(line)
    for option in options:
        print(f"{option:<{maxLength}}")
    print(line)

# def main():
#     while True:
#         displayMenu()
#         try:
#             userChoice = int(input("¿Cuál es su elección?: "))
#             if userChoice == 1:
#                 registerExpense()
#             elif userChoice == 2:
#                 listExpenses()
#             elif userChoice == 3:
#                 calculateTotal()
#             elif userChoice == 4:
#                 generateReport()
#             elif userChoice == 5:
#                 print("Gracias por usar el simulador. ¡Hasta pronto!")
#                 break
#             else:
#                 print("Por favor, seleccione una opción válida (1-5).")
#         except ValueError:
#             print("Entrada inválida. Por favor, ingrese un número del 1 al 5.")
#         except KeyboardInterrupt:
#             print("\nInterrupción detectada. Por favor, use la opción 5 para salir.")

# if __name__ == "__main__":
#     main()
displayMenu()