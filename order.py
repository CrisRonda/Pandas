import pandas as pd
import numpy as np

df_data = pd.read_csv('Data.csv', encoding="ISO-8859-1")
# Columna para seleccion
df_data.set_index("Date", inplace=True)
df_data = df_data.replace(np.nan, 0)
df_data = df_data.replace("N/A", "0")
df_data = df_data.replace("NR", "0")
df_data['WRank'] = df_data.WRank.astype(int)
df_data['LRank'] = df_data.WRank.astype(int)
df_data['W1'] = df_data.WRank.astype(int)
selection = df_data.loc[(df_data['WRank'] > 20) & (df_data['WRank'] <= 45), [
    "Winner", "WRank", 'LRank', "W1"]]
print(selection.index)
# Ordenamiento sin numpy
# order_by_WRank = selection.sort_values(by=["WRank"], ascending=False)
# Ordenamiento con numpy en todas las columnas
order_np = pd.DataFrame(np.sort(selection.values, axis=0),
                        index=selection.index, columns=selection.columns)
print(order_np)
