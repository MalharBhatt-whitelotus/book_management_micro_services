import sqlite3
from datetime import datetime
from passlib.context import CryptContext
conn = sqlite3.connect("user_services/user.db")
cursor = conn.cursor()
admin_pass = "admin123"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password = pwd_context.hash(admin_pass)
created_at = datetime.now().utcnow()
cursor.execute("""
INSERT INTO users (name, username, email, password_hash, role, created_at)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    "Administrator",
    "admin",
    "a@gmail.com",
    password,      # Plain text (not recommended)
    "admin",
    created_at
))

conn.commit()
conn.close()

print("Admin user inserted successfully.")