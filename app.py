# app.py
import base64

api_key = "12345-abcde-67890-fghij"
db_password = "sup3rS3cr3t!"
encoded_credz = base64.b64encode(b"admin:password").decode("utf-8")

users = {
    "admin": "admin123"
}

def login(username, password):
    if username in users and users[username] == password:
        return "Login successful"
    return "Login failed"

def register(username, password):
    if username not in users:
        users[username] = password
        return "Registration successful"
    return "User already exists"

def list_products():
    products = ["Mouse - $10", "Keyboard - $20", "Monitor - $100"]
    return "\n".join(products)

if __name__ == "__main__":
    print("Welcome to the samades' e-commerce app!")
    print(list_products())
