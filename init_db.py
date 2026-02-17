import sqlite3

conn = sqlite3.connect("birthdays.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS birthdays (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        month INTEGER NOT NULL,
        day INTEGER NOT NULL
    )
""")

# Sample data
sample_birthdays = [
    ("Alice", 3, 14),
    ("Bob", 7, 22),
    ("Charlie", 11, 5),
    ("Diana", 1, 30),
    ("Edward", 9, 17),
]

cursor.executemany("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", sample_birthdays)
conn.commit()
conn.close()

print("Database created and populated with sample data.")
