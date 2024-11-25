from modules.utils.fileHandler import readJSON, writeJSON

def registerExpense():
    filePath = 'databases/expenses.json'
    data = readJSON(filePath)
    
    try:
        date = input("Ingrese la fecha del gasto (DD-MM-AA): ")
        amount = float(input("Ingrese el monto del gasto: "))
        currency = input("Ingrese la moneda (COP o USD): ").upper()
        category = input("Ingrese la categoría del gasto: ")
        description = input("Ingrese una descripción del gasto (opcional): ")

        newExpense = {
            "fecha": date,
            "monto": int(amount) if currency == "COP" else round(amount, 2),
            "moneda": currency,
            "categoría": category,
            "descripción": description
        }

        data["gastos"].append(newExpense)
        writeJSON(filePath, data)
        print("Gasto registrado exitosamente.")

    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar los datos correctamente.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida. Gasto no registrado.")