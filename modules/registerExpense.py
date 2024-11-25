from modules.utils.fileHandler import readJSON, writeJSON

def registerExpense():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    try:
        print("Registro de un nuevo gasto:")
        date = input("Ingrese la fecha del gasto (DD-MM-AA): ")
        amount = float(input("Ingrese el monto del gasto: "))
        currency = input("Ingrese la moneda del gasto (COP/USD): ").strip().upper()
        category = input("Ingrese la categoría del gasto (Ej.: Alimentación, Transporte): ").strip()
        description = input("Ingrese una descripción breve (opcional): ").strip()

        if currency not in ["COP", "USD"]:
            print("Moneda no válida. Use COP o USD.")
            return

        newExpense = {
            "fecha": date,
            "monto": amount if currency == "COP" else round(amount, 2),
            "moneda": currency,
            "categoría": category,
            "descripción": description or "Sin descripción"
        }

        expenses["gastos"].append(newExpense)
        writeJSON(filePath, expenses)

        print("¡Gasto registrado exitosamente!")
    except ValueError:
        print("Monto inválido; por favor ingrese un número.")
    except Exception as e:
        print(f"Error al registrar el gasto: {e}")