# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx",
# agrega una columna llamada "Mat_Fisica" que contiene valores aleatorios entre 0 y 100 con un decimal,
# ordena la tabla por el campo "Nombre", cuenta el número de registros y campos,
# identifica los campos numéricos, calcula el promedio de las calificaciones en cada materia,
# encuentra la calificación máxima y mínima en cada materia, muestra los nombres de los alumnos correspondientes,
# genera un gráfico de barras comparativo, y guarda el archivo actualizado con un nuevo nombre "calificaciones_alumnos_actualizado.xlsx".

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Generar valores aleatorios para la columna "Mat_Fisica"
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, df.shape[0]), 1)

# Ordenar la tabla por el campo "Nombre"
df = df.sort_values(by='Nombre')

# Contar el número de registros (filas) y campos (columnas)
num_registros = df.shape[0]
num_campos = df.shape[1]

# Identificar los campos numéricos
campos_numericos = df.select_dtypes(include=[np.number]).columns.tolist()

# Calcular el promedio de las calificaciones en cada materia
promedios = df[campos_numericos].mean()

# Encontrar la calificación máxima y mínima en cada materia
maximas = df[campos_numericos].max()
minimas = df[campos_numericos].min()

# Encontrar los nombres de los alumnos con la calificación máxima y mínima en cada materia
alumnos_max = df.loc[df[campos_numericos].idxmax(), 'Nombre'].reset_index(drop=True)
alumnos_min = df.loc[df[campos_numericos].idxmin(), 'Nombre'].reset_index(drop=True)

# Imprimir el número de registros y campos
print(f"Número de registros: {num_registros}")
print(f"Número de campos: {num_campos}")

# Imprimir los campos numéricos
print("Campos numéricos:", campos_numericos)

# Imprimir los promedios de las calificaciones
print("Promedios de calificaciones en cada materia:")
print(promedios)

# Imprimir las calificaciones máximas y los nombres de los alumnos correspondientes
print("Calificaciones máximas y nombres de los alumnos correspondientes:")
for materia in maximas.index:
    print(f"{materia}: {maximas[materia]} - {alumnos_max[materia]}")

# Imprimir las calificaciones mínimas y los nombres de los alumnos correspondientes
print("Calificaciones mínimas y nombres de los alumnos correspondientes:")
for materia in minimas.index:
    print(f"{materia}: {minimas[materia]} - {alumnos_min[materia]}")

# Generar un gráfico de barras comparativo
plt.figure(figsize=(10, 6))
promedios.plot(kind='bar')
plt.title('Promedio de calificaciones por materia')
plt.xlabel('Materias')
plt.ylabel('Promedio')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Guardar el gráfico
plt.savefig('promedio_calificaciones.png')
plt.show()

# Guardar el archivo actualizado con un nuevo nombre
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False)

print("Columna 'Mat_Fisica' agregada, tabla ordenada por 'Nombre', promedios calculados, calificaciones máximas y mínimas encontradas, gráfico generado y archivo guardado como 'calificaciones_alumnos_actualizado.xlsx'.")
