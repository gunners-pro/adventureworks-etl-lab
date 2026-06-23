from pathlib import Path
import pandas as pd
from pyodbc import Connection

ROOT = Path(__file__).resolve().parent.parent

def extract_products(conn: Connection) -> None:
    df = pd.read_sql(
        """
        SELECT dp.*, 
        dps.ProductSubcategoryAlternateKey, dps.EnglishProductSubcategoryName, dps.SpanishProductSubcategoryName, dps.FrenchProductSubcategoryName, dps.ProductCategoryKey,
        dpc.ProductCategoryAlternateKey, dpc.EnglishProductCategoryName, dpc.SpanishProductCategoryName, dpc.FrenchProductCategoryName
        FROM DimProduct AS dp
        INNER JOIN DimProductSubcategory AS dps ON dp.ProductSubcategoryKey = dps.ProductSubcategoryKey
        INNER JOIN DimProductCategory AS dpc ON dps.ProductCategoryKey = dpc.ProductCategoryKey
        """,
        conn
    )    

    df.to_parquet(ROOT / "data/raw/products.parquet")
    print(f"Successfully Save products as parquet, total registers: {len(df)}")