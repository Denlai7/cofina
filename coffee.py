import sqlite3
conn = sqlite3.connect('coffee.db', check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS coffee_types (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            price REAL
        )
    ''')
    conn.commit()
    
    
def get_all_coffee():
    return cursor.execute('SELECT * FROM coffee_types').fetchall()
    
def remove_coffee(coffee_id):
    cursor.execute('DELETE FROM coffee_types WHERE id = ?', (coffee_id,))
    conn.commit()

def insert_data(name, description, price):
    cursor.execute('INSERT INTO coffee_types (name, description, price) VALUES (?, ?, ?)', (name, description, price))
    conn.commit()
