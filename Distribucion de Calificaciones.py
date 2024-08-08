# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx",
# identifica los campos numéricos y genera histogramas para mostrar la distribución de las calificaciones en cada materia.

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Identificar los campos numéricos
campos_numericos = df.select_dtypes(include=[float, int]).columns.tolist()

# Generar histogramas para mostrar la distribución de las calificaciones en cada materia
for materia in campos_numericos:
    plt.figure(figsize=(10, 6))
    plt.hist(df[materia], bins=20, edgecolor='k', alpha=0.7)
    plt.title(f'Distribución de calificaciones en {materia}')
    plt.xlabel('Calificaciones')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y')

    # Guardar cada histograma
    plt.savefig(f'distribucion_{materia}.png')
    plt.show()

print("Histogramas generados para la distribución de las calificaciones en cada materia.")
