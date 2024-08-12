import sqlite3

print("\A w \A eee")
conn = sqlite3.connect('example.db')
"""
table_name = input("Enter the name of the table: ")
columns = input("Enter the columns of the table: ")
query = f"CREATE TABLE {table_name} ({columns})"
conn.execute(query)
"""


x=0
while x==0:
  id = input("Enter the ID: ")
  name = input("Enter the name: ")
  conn.execute(f"INSERT INTO table_name (id, nombre) VALUES ({id}, '{name}')")

cursor = conn.execute("SELECT * FROM Pendientes")
for row in cursor:
    print(row)

conn.close()

