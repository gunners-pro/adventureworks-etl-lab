import os
from pyodbc import Connection, connect

from .errors import MissingEnvironmentVariableError

def get_connection() -> Connection:
    DB_SERVER = os.getenv("DB_SERVER")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    if not DB_SERVER:
        raise MissingEnvironmentVariableError("DB_SERVER enviroment variable must be set.")
    if not DB_NAME:
        raise MissingEnvironmentVariableError("DB_NAME enviroment variable must be set.")
    if not DB_USER:
        raise MissingEnvironmentVariableError("DB_USER enviroment variable must be set.")
    if not DB_PASSWORD:
        raise MissingEnvironmentVariableError("DB_PASSWORD enviroment variable must be set.")

    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD};"
        "TrustServerCertificate=yes;"
    )
    
    return connect(conn_str)    