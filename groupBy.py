import pandas as pd


data = pd.read_csv('IMDB-Movie-Data.csv', encoding="ISO-8859-1")
df = pd.DataFrame(data)
index_max_duration = df['Runtime (Minutes)'].idxmax()
info_max_duration = df.loc[index_max_duration,
                           ["Title", "Runtime (Minutes)", "Votes"]]
print("\n\n***********La pelicula con más duración***********")
print("La pelicula ", info_max_duration["Title"], "dura: ",
      info_max_duration["Runtime (Minutes)"], " minutos.", " Ademas, tiene ", info_max_duration["Votes"], "votos a favor")
# Agrupación por generos de peliculas
df_generes = df.groupby(['Genre'])[['Votes']].sum()
# Obtengo el index de los generos más gustados
index_df_generes = df_generes.idxmax()
# Obtengo el mayor número de votos
max_votes = df_generes["Votes"].max()

print("\n\n***********Las peliculas más gustadas***********")
print("Las peliculas más votadas y gustadas fueron: ",
      index_df_generes["Votes"], " con ", max_votes, " votos")

# Agrupo todos los directores por nombre y por valores
df_director = df.groupby(['Director'])[["Revenue (Millions)"]]
# Sumo cuanto gastaron en todas sus peliculas
df_director_total = df_director.sum()

# Saco el promedio que gasta cada director por pelicula
df_director_mean = df_director.mean()

# Director que gasto más en un periodo de tiempo
df_director_total_id = df_director_total.idxmax()
df_director_total_money = df_director_total.loc[df_director_total_id].values[0]

# Director que gasta más en un promedio por pelicula
df_director_mean_id = df_director_mean.idxmax()
df_director_mean_money = df_director_mean.loc[df_director_mean_id].values[0]

print("\n\n***********Presupuesto por cada director***********")
print("El director que gasta más en este periodo de tiempo es: ",
      df_director_total_id[0], " y gasta: $", round(df_director_total_money[0], 2))
print("El director que gasta más en promedio por pelicula es: ",
      df_director_mean_id[0], " y gasta: $", round(df_director_mean_money[0], 2))

# Agrupacion por genero que más gasta
df_gener_money = df.groupby(['Genre'])[["Revenue (Millions)"]].sum()
# Nombre(s) de los generos que más gastan
id_genre_money = df_gener_money.idxmax().values[0]
# Dinero que gastan
gener_money = df_gener_money.loc[id_genre_money].values[0]
print("\n\n***********Genero que gasta más dinero***********")
print("Los generos que más gastan son: ",
      id_genre_money, " y gastan: $", round(gener_money, 2))

# Agrupacion por año que más se gasto
df_year = df.groupby(["Year"])[["Revenue (Millions)"]].sum()
id_df_year = df_year.idxmax().values[0]
year_money = df_year.loc[id_df_year].values[0]
print("\n\n***********El año que gasto más dinero***********")
print("El años que se gasto más es: ",
      id_df_year, " y se gastó: $", round(year_money, 2))
