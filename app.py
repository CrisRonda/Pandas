
#!/usr/bin/env python3
# .*. coding: utf-8 .*.
import pandas as pd
import numpy as np

data_csv = pd.read_csv('Data.csv', encoding="ISO-8859-1")

# Info de la data del csv
print(data_csv.info())
print("\n"*2)

df_data = pd.DataFrame(data_csv)

# Reemplazo los valores NaN por 0
df_data = df_data.replace(np.nan, 0)

# Reemplazo los N/A, NR valores en todas las columnas (en específico WRank, LRank & LPts )
df_data = df_data.replace("N/A", "0")
df_data = df_data.replace("NR", "0")

# Cambio el tipo de datos de las columnas de los sets y el ranking
df_data['Wsets'] = df_data.Wsets.astype(int)
df_data['WRank'] = df_data.WRank.astype(int)
df_data.dropna(how="any", inplace=True)

# Estadisticas
print(df_data.describe(include=[int]).transpose())
