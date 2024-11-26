from datetime import datetime, timedelta
import json

def calculateWeek(filePath):
    try:
        # Leer el JSON
        with open(filePath, 'r') as file:
            expenses = json.load(file)
        
        # Validar si hay datos
        if not expenses:
            print("No hay gastos registrados.")
            return

        # Obtener fecha de hoy y rango de la semana
        today = datetime.today().date()
        startOfWeek = today - timedelta(days=7)

        # Filtrar por rango semanal
        totalWeek = sum(
            expense['monto'] for expense in expenses 
            if startOfWeek <= datetime.strptime(expense['fecha'], '%Y-%m-%d').date() <= today
        )

        print(f"El total de gastos de la semana es: COP {totalWeek}")
    except Exception as e:
        print(f"Ocurrió un error al calcular los gastos: {e}")