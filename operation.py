# Este programa realiza:
# 1) Revisa el valor actual con el anterior y con el mayor de todos (por defecto el primero es el mayor)
# 2) Si se el numero actual cumple con las condiciones anteriores
#   se resta el numero actual con el mayor y se actualiza el mayor
#   sino se guarda con 0
# 3) Sacamos la diferencia entre filas y finalmente sacamos la suma de los valores no negativos
# 4) Imprimimos por pantalla

import pandas as pd

data = pd.read_csv('minutos.csv', encoding="ISO-8859-1")
df = pd.DataFrame(data)

higer = df.loc[0, 'B']
# diferencia entre row y row
df['Partial sum'] = df['B'].diff(1)

for iter in range(1, len(df)):
    iter_now = df.loc[iter, 'B']
    iter_before = df.loc[iter-1, 'B']
    if iter_now > iter_before and iter_now > higer:
        df.loc[iter, 'dB'] = iter_now-higer
        higer = iter_now
    else:
        df.loc[iter, 'dB'] = 0
sum = df['dB'].sum()
partial_sum = df.loc[df['Partial sum'] > 0, 'Partial sum'].sum()
print(df)
print('La suma de la columna dB es ', sum)
print('La suma parcial Partial sum es ', partial_sum)
# Exportar los datos
# df.reset_index().to_csv('Export.csv',header=True,index=False)
