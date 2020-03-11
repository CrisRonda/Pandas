# Condicionales con loc

Antes de empezar debes seleccionar una columna para manejar los datos

`data_csv.set_index("Location", inplace=True)`

## Condicional básica y presentación de dos columnas

`selection = data_csv.loc[data_csv['WRank'] == '65', ['Winner', 'WRank']]`

# Condicionales multiples para busquedas en CVS

`selection = data_csv.loc[(data_csv['WRank'] == '65')& (data_csv['Winner'] =='Llodra M.'), ["WRank",'Winner']]`
