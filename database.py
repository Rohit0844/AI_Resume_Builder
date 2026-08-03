import sqlite3

# Connect to database
conn = sqlite3.connect("database.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    skills TEXT,
    education TEXT,
    projects TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")