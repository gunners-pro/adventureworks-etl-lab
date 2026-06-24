from pathlib import Path
import pandas as pd
from pyodbc import Connection

ROOT = Path(__file__).resolve().parent.parent

def extract_products(conn: Connection) -> None:
    with open(ROOT / "src/sql/extract_products.sql", "r") as file:
        sql_query = file.read()

    df = pd.read_sql_query(sql_query, conn)
    df.to_parquet(ROOT / "data/raw/products.parquet")
    print(f"Successfully Save products as parquet, total registers: {len(df)}")

def extract_customers(conn: Connection) -> None:
    with open(ROOT / "src/sql/extract_customers.sql", "r") as file:
        sql_query = file.read()

    df = pd.read_sql_query(sql_query, conn)
    df.to_parquet(ROOT / "data/raw/customers.parquet")
    print(f"Successfully Save customers as parquet, total registers: {len(df)}")

def extract_factinternetsales(conn: Connection) -> None:
    with open(ROOT / "src/sql/extract_factinternetsales.sql", "r") as file:
        sql_query = file.read()
    
    df = pd.read_sql_query(sql_query, conn)
    df.to_parquet(ROOT / "data/raw/internet_sales.parquet")
    print(f"Successfully Save internet_sales as parquet, total registers: {len(df)}")