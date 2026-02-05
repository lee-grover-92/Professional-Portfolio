import pandas as pd
import pymysql

# Connect to MySQL
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Weecekrimp92@@',
    database='pet_insurance'
)

# List of views to export
views = [
    'fact_claims_summary',
    'dim_customers',
    'dim_products',
    'fact_vet_costs'
]

# Export each view to CSV
for view in views:
    df = pd.read_sql(f"SELECT * FROM {view}", conn)
    df.to_csv(f'C:/Users/leebe/Documents/VScode/pet_data_project/data/processed/{view}.csv', index=False)

conn.close()
