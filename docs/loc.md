# loc[]

## Seleccion de la columna para el filtro

`data_csv.set_index("Round", inplace=True)`
`data_in_Atlanta_and_Surface = data_csv.loc['Atlanta', 'Surface']`

## Seleccion amplia 1er [Contiene lo que queremos buscar en la columna][columnas que queremos mostrar]

`data_selection = data_csv.loc[['Quarterfinals', '1st Round'],['Location', 'Winner']]`

## Seleccion amplia entre columnas a presentar, notar que no cuenta con []

`data_selection = data_csv.loc[['Quarterfinals', '1st Round'],'Location': 'Date']`

# Seleccion de datos en columna a través de un String

`data_selection = data_csv.loc[data_csv['Winner'].str.endswith("S.")]`
