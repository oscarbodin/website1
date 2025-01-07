import sqlite3
import pandas as pd

# Connect to the .db file
conn = sqlite3.connect('instance/database.db')  # Replace with your .db file path

# Query to get all table names
query1 = "SELECT * FROM user"
query2 = "SELECT * FROM note"

df1 = pd.read_sql(query1, conn)
df2 = pd.read_sql(query2, conn)

print(df1)
print(df2)
# Close the connection
conn.close()
