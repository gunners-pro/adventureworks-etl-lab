import os

from sqlalchemy import create_engine, Engine

from .errors import MissingEnvironmentVariableError

def get_connection() -> Engine:
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

    DRIVER = "ODBC Driver 18 for SQL Server"
    
    connection_string = f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver={DRIVER}&TrustServerCertificate=yes"
    
    return create_engine(connection_string)