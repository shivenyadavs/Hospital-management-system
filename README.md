# Hospital-management-system

# Connecting Python with MySQL

Python and MySQL can be connected to create powerful applications that interact with databases seamlessly. Below are the steps to establish a connection and perform operations.

---

### 1. Why Connect Python with MySQL?
```
- **Data Management**: Handle data storage and retrieval for applications.
- **Dynamic Applications**: Backend support for apps like hospital management systems.
- **Automation**: Perform database operations programmatically.
```

---

### 2. Required Libraries
Install the required libraries to connect Python with MySQL:
```
- **MySQL Connector/Python** (Official):
  pip install mysql-connector-python
```
```
- Alternatively, you can use **PyMySQL**:
  pip install pymysql
```

---

### 3. Steps to Connect Python with MySQL

#### Step 1: Import the Library
```python
import mysql.connector
```

#### Step 2: Establish a Connection
Provide the required credentials such as `host`, `user`, `password`, and optionally the `database` name:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"  # Optional
)

if conn.is_connected():
    print("Connected to MySQL")
```

#### Step 3: Create a Cursor
A cursor allows you to execute SQL queries:
```python
cursor = conn.cursor()
```

#### Step 4: Execute SQL Queries
- **Create a Table**:
  ```python
  cursor.execute("""
  CREATE TABLE patients (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100),
      age INT,
      gender VARCHAR(10)
  )
  """)
  ```

- **Insert Data**:
  ```python
  cursor.execute("INSERT INTO patients (name, age, gender) VALUES (%s, %s, %s)", ("John Doe", 30, "Male"))
  conn.commit()  # Commit changes
  ```

- **Fetch Data**:
  ```python
  cursor.execute("SELECT * FROM patients")
  for row in cursor.fetchall():
      print(row)
  ```

#### Step 5: Close the Connection
Always close the cursor and connection after completing the operations:
```python
cursor.close()
conn.close()
```

---

### 4. Full Example Code
Here’s an example that integrates all steps:
```python
import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="password123",
    database="hospital_db"
)

cursor = conn.cursor()

# Insert data into the table
cursor.execute("INSERT INTO patients (name, age, gender) VALUES (%s, %s, %s)", ("Alice", 28, "Female"))
conn.commit()

# Fetch and display all records
cursor.execute("SELECT * FROM patients")
for row in cursor.fetchall():
    print(row)

# Close the connection
cursor.close()
conn.close()
```

---

### 5. Security Best Practices
```
- **Use Prepared Statements**: Avoid SQL injection:
  cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```
```
- **Secure Credentials**: Store database credentials securely, e.g., in environment variables.
- **Use Connection Pools**: For large-scale applications, manage database connections efficiently.
```

---

### 6. Advanced Tools
```
- **SQLAlchemy**: For Object Relational Mapping (ORM).
- **DBeaver/MySQL Workbench**: Tools for visual database management.
```

Feel free to adapt this setup for your **Hospital Management System** or other projects!
