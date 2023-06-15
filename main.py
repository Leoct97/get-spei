from conexion.config import conexion
import pyodbc
import pandas as pd

try:
    sucursal = "exec sp_rpt_cierre_cajas '00006';"
    df = pd.read_sql_query(sucursal, conexion.engine)
    df.to_json(orient="records")
    df[["SUCURSAL", "CAJERO", "ESTATUS", "CAJA", "EJECUTIVO"]]
    print(df)
except pyodbc.Error as ex:
    print("no se ha podido conectar a la base de datos", ex)
