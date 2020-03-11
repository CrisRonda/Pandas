# Borrar una row
`filas = len(data_frame.index)`

`df = data_frame.drop(data_frame.index[[filas-1], inplace=True])`