import pandas as pd
import sqlite3

ods_file_path = "/home/cedrics/Downloads/Daten-Mittwoch.ods"

df_sheet1 = pd.read_excel(ods_file_path, engine="odf", sheet_name=0)
df_sheet2 = pd.read_excel(ods_file_path, engine="odf", sheet_name=1)

df_sheet1_preview = df_sheet1.head()
df_sheet2_preview = df_sheet2.head()

db_connection = sqlite3.connect("/home/cedrics/Downloads/Daten_Mittwoch.db")

df_sheet1.to_sql("Regressionsdaten", db_connection, if_exists="replace", index=False)
df_sheet2.to_sql("Inventar", db_connection, if_exists="replace", index=False)

print(df_sheet1_preview)
print(df_sheet2_preview)

sum_query = """
SELECT Kategorie, SUM(Anzahl) AS Gesamtsumme
FROM Inventar
GROUP BY Kategorie;
"""

max_price_query = """
SELECT Kategorie, MAX(Einzelpreis) AS MaxPreis
FROM Inventar
GROUP BY Kategorie;
"""

sum_result = pd.read_sql_query(sum_query, db_connection)
max_price_result = pd.read_sql_query(max_price_query, db_connection)

print(sum_result)
print(max_price_result)

