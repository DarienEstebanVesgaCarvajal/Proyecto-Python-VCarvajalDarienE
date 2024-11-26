Claro, aquí tienes el instructivo completo en formato para un archivo `README.md`:

```markdown
# Simulador de Gasto Diario

Este programa permite registrar y generar reportes de los gastos en diferentes rangos de tiempo, ya sea semanal o mensual. Los datos de los gastos se almacenan en un archivo JSON y se pueden visualizar a través de la consola en formato tabular.

## Funcionalidades

1. **Ingreso de Gastos:**
   El programa permite al usuario registrar gastos con la siguiente información:
   - **Nombre del gasto:** Descripción breve del gasto (por ejemplo, "Compra de alimentos").
   - **Monto:** Valor numérico del gasto (puede ser en cualquier moneda).
   - **Fecha:** La fecha en la que ocurrió el gasto, en formato `YYYY-MM-DD` (por ejemplo, `2024-11-25`).
   - **Categoría:** La categoría del gasto (por ejemplo, "Alimentos", "Transporte", "Entretenimiento", etc.).

   **Los gastos registrados se guardan en un archivo JSON**, que guarda un historial de todos los gastos ingresados. Este archivo puede ser cargado posteriormente para generar reportes.

2. **Generación de Reportes:**
   El programa permite generar dos tipos de reportes de los gastos registrados:
   - **Reporte Semanal:**
     Muestra los gastos registrados durante la última semana (últimos 7 días desde la fecha actual). Incluye el total de los gastos de la semana y un desglose detallado de cada gasto con su nombre, monto, categoría y fecha.
   - **Reporte Mensual:**
     Muestra los gastos registrados durante el mes actual. Incluye el total de los gastos del mes y un desglose detallado de cada gasto con su nombre, monto, categoría y fecha.

3. **Estructura del Archivo JSON:**
   El archivo JSON donde se almacenan los datos tiene la siguiente estructura:
   ```json
   [
     {
       "nombre": "Compra de alimentos",
       "monto": 50.00,
       "fecha": "2024-11-25",
       "categoria": "Alimentos"
     },
     {
       "nombre": "Transporte público",
       "monto": 10.00,
       "fecha": "2024-11-24",
       "categoria": "Transporte"
     }
   ]
   ```

   Cada elemento del archivo es un objeto que representa un gasto con las claves:
   - **nombre:** Descripción del gasto.
   - **monto:** Valor del gasto.
   - **fecha:** Fecha en formato `YYYY-MM-DD`.
   - **categoria:** Categoría del gasto.

4. **Manejo de Errores:**
   El programa incluye un manejo de excepciones para asegurarse de que el archivo JSON esté correctamente estructurado. En caso de que falte alguna clave esperada (como "nombre", "monto", "fecha" o "categoria"), se mostrará un mensaje de error. Además, si ocurre cualquier otro tipo de error, se mostrará un mensaje de error general.

5. **Generación del Reporte:**
   Cuando el usuario solicita generar un reporte (semanal o mensual), el programa:
   - **Lee el archivo JSON** para obtener los datos de los gastos registrados.
   - **Filtra los gastos** según el rango de fechas correspondiente (últimos 7 días para el reporte semanal y mes actual para el reporte mensual).
   - **Calcula el total de los gastos** en el rango de fechas especificado.
   - **Muestra el reporte en consola**, con el total de los gastos y un desglose de cada uno de los gastos registrados, con su nombre, monto, categoría y fecha.

## Funciones Principales del Programa

1. **`generateWeek(filePath)`**
   - Genera un reporte de los gastos registrados en la última semana (últimos 7 días desde la fecha actual).
   - Muestra el total de los gastos de la semana y un desglose detallado de cada gasto con su nombre, monto, categoría y fecha.

2. **`generateMonth(filePath)`**
   - Genera un reporte de los gastos registrados en el mes actual.
   - Muestra el total de los gastos del mes y un desglose detallado de cada gasto con su nombre, monto, categoría y fecha.

## Ejemplo de Ejecución

Supongamos que el archivo JSON contiene los siguientes gastos:
```json
[
  {
    "nombre": "Compra de alimentos",
    "monto": 50.00,
    "fecha": "2024-11-25",
    "categoria": "Alimentos"
  },
  {
    "nombre": "Transporte público",
    "monto": 10.00,
    "fecha": "2024-11-24",
    "categoria": "Transporte"
  },
  {
    "nombre": "Cine",
    "monto": 20.00,
    "fecha": "2024-11-15",
    "categoria": "Entretenimiento"
  }
]
```

- **Generación del reporte semanal:**
  Si hoy es `2024-11-26`, el reporte semanal incluirá los gastos del `2024-11-19` al `2024-11-26`, es decir, solo los gastos de `Transporte público` y `Compra de alimentos`.

  El reporte se verá de la siguiente manera:
  ```
  Reporte Semanal:
  Total de la semana: 60.00
  Compra de alimentos - 50.00 - Alimentos - 2024-11-25
  Transporte público - 10.00 - Transporte - 2024-11-24
  ```

- **Generación del reporte mensual:**
  Si se genera el reporte mensual, incluirá todos los gastos desde el `01-11-2024` hasta la fecha actual (`2024-11-26`), es decir, los tres gastos mencionados.

  El reporte mensual se verá así:
  ```
  Reporte Mensual:
  Total del mes: 80.00
  Compra de alimentos - 50.00 - Alimentos - 2024-11-25
  Transporte público - 10.00 - Transporte - 2024-11-24
  Cine - 20.00 - Entretenimiento - 2024-11-15
  ```

## Recomendaciones

- Asegúrate de ingresar las fechas de los gastos en el formato `YYYY-MM-DD` para evitar errores de formato.
- Mantén el archivo JSON actualizado para obtener reportes precisos.
- Revisa el reporte generado para asegurarte de que los gastos estén correctamente reflejados según el rango de fechas.