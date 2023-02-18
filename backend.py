import sqlite3

# Criando DB
dbase = sqlite3.connect('filmes.db')
cursor = dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS filmes(
                  ID INT PRIMARY KEY NOT NULL,
                  NAME TEXT NOT NULL)''')

# Aplicando mudanças na DB
dbase.commit()


def write(ID, NAME):
    cursor.execute(''' INSERT into filmes(ID, NAME) VALUES(?,?)''', (ID, NAME))
    dbase.commit()


def delete(x):
    cursor.execute('''SELECT NAME from filmes where NAME =?''', x)
    dbase.commit()
