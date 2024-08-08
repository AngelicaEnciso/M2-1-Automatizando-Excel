# Este programa lee un archivo de Excel llamado "calificaciones_alumnos.xlsx" que contiene los nombres de los alumnos y sus calificaciones
# en tres materias: Cálculo Integral, Programación Orientada a Objetos y Estructura de Datos. Luego, grafica las calificaciones para cada alumno
# asegurando que las etiquetas en el eje X no se encimen.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Definir los nombres de las columnas de calificaciones
calificaciones_columns = ['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']

# Crear una figura y ejes para la gráfica
fig, ax = plt.subplots(figsize=(10, 6))

# Definir el número de alumnos
num_alumnos = len(df)

# Generar un arreglo de índices para las posiciones en el eje X
indices = np.arange(num_alumnos)

# Ancho de las barras
bar_width = 0.25

# Graficar las calificaciones de cada materia con un desplazamiento en el eje X
ax.bar(indices, df['Mat_CalculoIntegral'], width=bar_width, label='Cálculo Integral')
ax.bar(indices + bar_width, df['Mat_ProgramacionOOP'], width=bar_width, label='Programación OOP')
ax.bar(indices + 2 * bar_width, df['Mat_EstructuraDatos'], width=bar_width, label='Estructura de Datos')

# Establecer las etiquetas del eje X
ax.set_xticks(indices + bar_width)
ax.set_xticklabels(df['Nombre'], rotation=45, ha='right')

# Agregar etiquetas y título
ax.set_xlabel('Alumnos')
ax.set_ylabel('Calificaciones')
ax.set_title('Calificaciones de los Alumnos')
ax.legend()

# Ajustar el layout para que las etiquetas no se encimen
plt.tight_layout()

# Mostrar la gráfica
plt.show()
