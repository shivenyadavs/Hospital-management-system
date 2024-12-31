import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        username="shiven",
        password="root",
        database="mydata"
    )
    print("Connection successful")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
