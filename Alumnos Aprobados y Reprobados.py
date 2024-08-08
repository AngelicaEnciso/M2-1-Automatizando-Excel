# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx",
# identifica los campos numéricos y determina cuántos alumnos aprobaron y reprobaron en cada materia,
# considerando una calificación mínima aprobatoria de 60.

import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Identificar los campos numéricos
campos_numericos = df.select_dtypes(include=[float, int]).columns.tolist()

# Calificación mínima aprobatoria
calificacion_minima = 60

# Determinar cuántos alumnos aprobaron y reprobaron en cada materia
resultados = {}
for materia in campos_numericos:
    aprobados = (df[materia] >= calificacion_minima).sum()
    reprobados = (df[materia] < calificacion_minima).sum()
    resultados[materia] = {'Aprobados': aprobados, 'Reprobados': reprobados}

# Imprimir los resultados
for materia, conteo in resultados.items():
    print(f"Materia: {materia}")
    print(f"  Alumnos aprobados: {conteo['Aprobados']}")
    print(f"  Alumnos reprobados: {conteo['Reprobados']}")
    print()
