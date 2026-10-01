import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Database engine: Ye SQLite file create karega (server install karne ki zaroorat nahi)
db_name = "olist.db"
engine = create_engine(f"sqlite:///{db_name}")

data_folder = "data"

# 2. Files mapping: File ka naam -> SQL table ka naam
files_to_tables = {
    "olist_orders_dataset.csv": "orders",
    "olist_customers_dataset.csv": "customers",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "payments",
    "olist_products_dataset.csv": "products",
    "product_category_name_translation.csv": "category_translation",
    "olist_sellers_dataset.csv": "sellers",
    "olist_order_reviews_dataset.csv": "reviews",
    "olist_geolocation_dataset.csv": "geolocation" 
}

print("--- Data Loading Shuru Ho Rha Hai ---")

for file_name, table_name in files_to_tables.items():
    file_path = os.path.join(data_folder, file_name)
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        # to_sql se pandas dataframe sidha SQL table ban jata hai
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        print(f" Table ban gayi: '{table_name}' | Total Rows: {len(df):,}")
    else:
        print(f" Warning: '{file_name}' data folder me nahi mili!")

print("\n Database 'olist.db' ready ho gaya!")