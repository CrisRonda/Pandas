# iloc

### Seccionar los datos de la fila 0 a la 5

`row_0_to_5 = data_csv.iloc[0: 5]`

### Seleccionar filas no consecutivas

`row_not_consecutive = data_csv.iloc[[100, 50, 25, 200, 400]]`

### Seleccionar columnas

`column_0_to_2 = data_csv.iloc[:, 0:3]`

### Seleccionar rangos de filas y columnas

`new_data = data_csv.iloc[0:5, 5:34]`

### Seleccionar filas y columnas no consecutivas

`column_not_consecutive = data_csv.iloc[[4, 5, 6, 7], [0, 2, 1]]`
