import sqlite3
import hashlib
import requests

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def execute_sql(conn, sql_file):
    try:
        with open(sql_file, 'r') as file:
            sql = file.read()
        cursor = conn.cursor()
        cursor.executescript(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    if row and row[0] == hash_password(password):
        return "Login successful"
    return "Login failed"

def register(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    if row is None:
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return "Registration successful"
    return "User already exists"

def check_mouse_stock():
    url = "https://api.selmankon.com/mouse/count"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        stock_count = response.json().get("count")
        return f"Mouse stock count: {stock_count}"
    else:
        return "Failed to retrieve mouse stock"

def main():
    database = "ecommerce.db"

    conn = create_connection(database)

    if conn is not None:
        execute_sql(conn, 'database.sql')

        # Register and login examples
        print(register(conn, "newuser", "newpassword123"))
        print(login(conn, "admin", "sha256hash1"))
        
        # Check mouse stock
        print(check_mouse_stock())
        
        conn.close()

if __name__ == "__main__":
    main()
