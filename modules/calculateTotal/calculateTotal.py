from modules.utils.fileHandler import readJSON

def filterExpenses():
    filePath = 'databases/expenses.json'
    expenses = readJSON(filePath)

    if not expenses["gastos"]:
        print("No hay gastos registrados.")
        return

    totalCOP = sum(expense["monto"] for expense in expenses["gastos"] if expense["moneda"] == "COP")
    totalUSD = sum(expense["monto"] for expense in expenses["gastos"] if expense["moneda"] == "USD")

    print(f"Total de gastos en COP: {totalCOP}")
    print(f"Total de gastos en USD: {totalUSD:.2f}")