import sqlite3

# Criando DB
dbase = sqlite3.connect('filmes_assistidos.db')
cursor = dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS filmes_assistidos(
                  ID INT PRIMARY KEY NOT NULL,
                  NAME TEXT)''')

# Aplicando mudanças na DB
dbase.commit()


def write(ID, NAME):
    cursor.execute('''INSERT INTO filmes_assistidos(ID, NAME) VALUES(?,?)''', (ID, NAME ))
    dbase.commit()


def delete(x):
    cursor.execute('''delete from filmes_assistidos where NAME=?''', x)
    dbase.commit()


def read_task():
    c = dbase.cursor()
    c.execute('''SELECT NAME from filmes_assistidos''')
    data = c.fetchall()
    dbase.commit()
    return data
