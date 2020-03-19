# between_time

Este es un ejemplo corto de como filtrar un Dataframe por medio de fechas

1. Modifico la columna LocalTime para hacer un parse de str a timestamp
   `df_extrat_data["LocalTime"] = pd.DatetimeIndex(df_extrat_data['LocalTime'])`
2. Set del nuevo index
   `df_extrat_data.set_index(keys='LocalTime', inplace=True)`
3. Fechas de inicio y fin
   `start_date = datetime.time(11, 18, 0)`
   `end_date = datetime.time(11, 19, 0)`
4. Filtro entre fechas y extraigo dos columnas
   `df_filter = df_extrat_data[["Price", "Source"]].between_time(start_date, end_date)`
