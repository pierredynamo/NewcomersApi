import sqlite3
import pandas as pd
# Step 1 load data file

df = pd.read_csv('count2.csv')

# Step 2 (optional) data Clean up
df.columns = df.columns.str.strip()

# Step 3 Create/connect to a SQlite database

connection = sqlite3.connect('db.sqlite3')

# Step 4 load data file to SQLite
# fail; replace; append
df.to_sql('api_countries', connection, if_exists='append')

connection.close()


