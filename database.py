import sqlite3

conn = sqlite3.connect('places2.db')
c = conn.cursor()
# c.execute('CREATE TABLE places(place text)')
#c.execute('CREATE TABLE user(email text, password text)')

#c.execute("INSERT INTO places (place) VALUES (?)", (''))

c.execute("INSERT INTO places VALUES ('') ")


conn.commit()

conn.close()
