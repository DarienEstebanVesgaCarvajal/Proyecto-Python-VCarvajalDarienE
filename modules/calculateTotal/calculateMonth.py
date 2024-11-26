from datetime import datetime
import json

def calculateMonth(filePath):
    try:
        # Leer el JSON
        with open(filePath, 'r') as file:
            expenses = json.load(file)
        
        # Validar si hay datos
        if not expenses:
            print("No hay gastos registrados.")
            return

        # Obtener el mes y año actuales
        today = datetime.today()
        currentMonth = today.month
        currentYear = today.year

        # Filtrar por el mes actual
        totalMonth = sum(
            expense['monto'] for expense in expenses 
            if datetime.strptime(expense['fecha'], '%Y-%m-%d').month == currentMonth and 
               datetime.strptime(expense['fecha'], '%Y-%m-%d').year == currentYear
        )

        print(f"El total de gastos del mes es: COP {totalMonth}")
    except Exception as e:
        print(f"Ocurrió un error al calcular los gastos: {e}")