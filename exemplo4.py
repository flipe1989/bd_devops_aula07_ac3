import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE teste (id integer, nome text not null, primary key (id))''')
c.execute('CREATE TABLE teste2 (id2 integer, nome2 text not null, primary key (id2))')


c.execute('''SELECT * 
                FROM sqlite_master AS m, pragma_table_info(m.name)
                WHERE tbl_name = 'teste2'
            ''')
for row in c.fetchall():
    print(row)
    print('coluna: ', row[6])
    print('tipo: ', row[7])
    print('pk: ', row[10])

conn.commit()
conn.close()