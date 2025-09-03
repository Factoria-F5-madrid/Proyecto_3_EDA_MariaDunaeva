import pandas as pd

# Reemplaza esta línea con la ruta a tu archivo CSV descargado
df = pd.read_csv('touristic_cities/data/raw/Worldwide Travel Cities Dataset (Ratings and Climate).csv')

# Mostrar si hay nombres de ciudad duplicados
duplicated = df[df.duplicated(subset=["city"], keep=False)]

if not duplicated.empty:
    print("Ciudades duplicadas:")
    print(duplicated["city"].value_counts())
else:
    print("No se encontraron ciudades duplicadas.")