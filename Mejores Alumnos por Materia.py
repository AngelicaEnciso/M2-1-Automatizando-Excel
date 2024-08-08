# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx",
# y muestra los nombres de los tres mejores alumnos en cada materia.

import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Identificar los campos numéricos (excepto el campo 'Nombre')
campos_numericos = df.select_dtypes(include=[float, int]).columns.tolist()
campos_numericos.remove('Nombre')  # Asegurarse de que 'Nombre' no esté en la lista de campos numéricos

# Mostrar los nombres de los tres mejores alumnos en cada materia
for materia in campos_numericos:
    # Ordenar los datos de la materia de mayor a menor calificación y seleccionar los tres primeros
    mejores_alumnos = df.nlargest(3, materia)[['Nombre', materia]]
    print(f"Tres mejores alumnos en {materia}:")
    print(mejores_alumnos)
    print()
