# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx",
# agrega una columna llamada "Mat_Fisica" que contiene valores aleatorios entre 0 y 100 con un decimal,
# ordena la tabla por el campo "Nombre", cuenta el número de registros y campos,
# identifica los campos numéricos, e imprime esta información antes de guardar el archivo actualizado
# con un nuevo nombre "calificaciones_alumnos_actualizado.xlsx".

import pandas as pd
import numpy as np

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

# Imprimir el número de registros y campos
print(f"Número de registros: {num_registros}")
print(f"Número de campos: {num_campos}")

# Imprimir los campos numéricos
print("Campos numéricos:", campos_numericos)

# Guardar el archivo actualizado con un nuevo nombre
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False)

print("Columna 'Mat_Fisica' agregada, tabla ordenada por 'Nombre' y archivo guardado como 'calificaciones_alumnos_actualizado.xlsx'.")
