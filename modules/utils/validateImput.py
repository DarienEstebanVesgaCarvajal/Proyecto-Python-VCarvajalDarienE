def validateNumberInput(prompt, allowNegative=False):
    while True:
        try:
            userInput = input(prompt).strip()
            number = float(userInput)
            if not allowNegative and number < 0:
                print("El número no puede ser negativo. Intente nuevamente.")
            else:
                return number
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

from datetime import datetime

def validateDateInput(prompt):
    while True:
        try:
            userInput = input(prompt).strip()
            validDate = datetime.strptime(userInput, "%d-%m-%y").date()
            return validDate
        except ValueError:
            print("Fecha inválida. Use el formato DD-MM-AA e intente nuevamente.")

def validateChoiceInput(prompt, choices):
    while True:
        userInput = input(prompt).strip()
        if userInput in choices:
            return userInput
        else:
            print(f"Opción inválida. Seleccione una de las siguientes: {', '.join(map(str, choices))}.")

def confirmAction(prompt):
    while True:
        userInput = input(prompt).strip().upper()
        if userInput in ['S', 'N']:
            return userInput == 'S'
        else:
            print("Entrada inválida. Responda con 'S' para sí o 'N' para no.")

def validateCategoryInput(prompt, categories):
    while True:
        userInput = input(prompt).strip().lower()
        if userInput in categories:
            return userInput
        else:
            print(f"Categoría inválida. Las opciones válidas son: {', '.join(categories)}.")
