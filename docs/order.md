# Ordenamiento
## Ordenamiento sin numpy
`order_by_WRank = selection.sort_values(by=["WRank"], ascending=False)`
## Ordenamiento con numpy en todas las columnas
¿Qué está pasando aquí? Simple, primero creamos un DataFrame el cual albergará los datos ordenados el primer argumento represental los valores de un dataframe existente.
`axis` ordenará los datos de las columnas luego añadimos el index y las columnas al dataframe
`order_np = pd.DataFrame(np.sort(selection.values, axis=0),index=selection.index, columns=selection.columns)`

