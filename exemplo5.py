import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

with open('create_table.sql', 'r') as content_file:
    content = content_file.read()
    c.execute(content)

c.execute('''SELECT * 
                FROM sqlite_master AS m, pragma_table_info(m.name)
            ''')

for row in c.fetchall():
    print(row)
    print('coluna: ', row[6])
    print('tipo: ', row[7])
    print('pk: ', row[10])

conn.commit()
conn.close()