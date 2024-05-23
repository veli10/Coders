import sqlite3

connection = sqlite3.connect('db1.db')

cursor = connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS  movies(name TEXT, releaseYear INT, rating FLOAT)")

# create_table()

# name = input('Film adi girin: ')
# releaseYear = int(input('Filmin cixma ilini girin: '))
# rating = float(input('Filmin reytinqini girin: '))

# def add_data(name, releaseYear, rating):
#     cursor.execute('INSERT INTO movies VALUES(?, ?, ?)', (name, releaseYear, rating))
#     connection.commit()

# add_data(name, releaseYear, rating)

def show_data():
    cursor.execute('SELECT * FROM movies')
    data = cursor.fetchall()
    for row in data:
        print(row)



def update_data(old_name, new_name):
    cursor.execute('UPDATE movies SET name=? WHERE name=?', (new_name, old_name))
    connection.commit()

update_data('Cahce', 'Cache')
show_data()
print('----------------------------------------------------------------')

def delete_movie(name):
    cursor.execute('DELETE FROM movies WHERE name=?', (name,))
    connection.commit()

delete_movie('Oldboy')
show_data()