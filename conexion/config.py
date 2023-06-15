from sqlalchemy import create_engine
import os


class config_sql:
    conexion = os.environ['DB_HOST']
    base = os.environ['DB_NAME']
    user = os.environ['DB_USER']
    pwd = os.environ['DB_PASS']
    connect = "mssql+pyodbc://"+user+":"+pwd+"@"+conexion+"/"+base+"?driver=ODBC+Driver+17+for+SQL+Server"


class conexion: 
    engine = create_engine(config_sql.connect)
    print("conexion exitosa")
