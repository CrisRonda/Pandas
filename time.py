import pandas as pd
import datetime

data = pd.read_csv("datosnum.csv")

df = pd.DataFrame(data)
df = df.fillna(0)
# Extraigo las columnas con valores de fechas
LocalTime = df['A'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
MarketTime = df['C'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')

# Extrayendo enteros y flotantes
Price = df['F'].str.extract('(\d+(?:\.\d+)?)')
Source = df['G'].str.extract('(\d+(?:\.\d+)?)')

# Declaro un nuevo dataframe para guardar los datos extraidos
df_extrat_data = pd.DataFrame()
df_extrat_data = df_extrat_data.fillna(0)
df_extrat_data['LocalTime'] = LocalTime[0].values
df_extrat_data['MarketTime'] = MarketTime[0].values
df_extrat_data['Price'] = Price[0].values
df_extrat_data['Source'] = Source[0].values

# Modifico la columna LocalTime para hacer un parse de str a timestamp
df_extrat_data["LocalTime"] = pd.DatetimeIndex(df_extrat_data['LocalTime'])
# Set del nuevo index
df_extrat_data.set_index(keys='LocalTime', inplace=True)
# Fechas de inicio y fin
start_date = datetime.time(11, 18, 0)
end_date = datetime.time(11, 19, 0)
# Filtro entre fechas y extraigo dos columnas
df_filter = df_extrat_data[["Price", "Source"]
                           ].between_time(start_date, end_date)
print(df_filter)
