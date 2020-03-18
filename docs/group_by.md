# GROUP BY
Nos permite hacer agrupaciones en columnas con datos similares.
## Sintaxis
En el ejemplo usamos las columnas `Genre` y `Revenue (Millions)` para saber que genero de peliculas gasta más dinero en la producción de las mismas.
`df_gener_money = df.groupby(['Genre'])[["Revenue (Millions)"]].sum()`
## Obtenemos Nombre(s) de los generos que más gastan
`id_genre_money = df_gener_money.idxmax().values[0]`
## Obtenemos el dinero que gastan
`gener_money = df_gener_money.loc[id_genre_money].values[0]`
`print("\n\n***********Genero que gasta más dinero***********")`
`print("Los generos que más gastan son: ", id_genre_money, " y gastan: $", round(gener_money, 2))`
