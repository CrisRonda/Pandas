# Leer Excel

`xls_file = pd.ExcelFile("name.xls")`
`print(xls_file.sheet_names)`

# Parse a un data frame de una hoja de Excel

`df= xls_file.parse('sheet_name')`