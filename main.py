import os
from dotenv import load_dotenv
from src.connection import get_connection
from src.extract import extract_products, extract_customers

load_dotenv()

os.makedirs("data/raw", exist_ok=True)

conn = get_connection()

extract_customers(conn)