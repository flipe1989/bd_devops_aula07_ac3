import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()
c.execute('''SELECT * FROM stocks''')

for row in c.fetchall():
    print(row)
    print('Data:', row[0])

conn.close()