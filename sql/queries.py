import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv("E:\Study Material\datascience_projects\sales-retail-analysis\sales-data-analysis\dataset\SuperMarket Analysis.csv")

# Create in-memory SQLite DB
conn = sqlite3.connect(":memory:")

# Push CSV to SQL table
df.to_sql("SalesDB", conn, index=False, if_exists="replace")

# Now you can run SQL queries
query = """
SELECT Payment, SUM(Sales) AS TotalSold
FROM SalesDb
GROUP BY Payment
ORDER BY TotalSold DESC;
"""
result = pd.read_sql_query(query, conn)
print(result)

df.to_sql("SalesDB", conn, index=False, if_exists="replace")

# Now you can run SQL queries
query = """
SELECT Payment, COUNT(*)
FROM SalesDB
GROUP BY Payment;
"""
result = pd.read_sql_query(query, conn)
print(result)