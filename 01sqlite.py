import sqlite3
conn=sqlite3.connect("mypractice.db")
cursor=conn.cursor()

conn.execute('''CREATE TABLE practicedic1 (id INT primary key, word TEXT NOT NULL, meaning TEXT NOT NULL)''')

print("Tabla creada exitosamente")