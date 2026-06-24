import os
from dotenv import load_dotenv
from src.connection import get_connection
from src.extract import extract_factinternetsales, extract_customers, extract_products

load_dotenv()

if __name__ == "__main__":
    os.makedirs("data/raw", exist_ok=True)
    conn = get_connection()
    extract_factinternetsales(conn)
    extract_customers(conn)
    extract_products(conn)
    conn.dispose()
    print("All data extracted successfully.")
