import sqlite3

conn = sqlite3.connect('user2.db')
c = conn.cursor()
# c.execute('CREATE TABLE places(place text)')
#c.execute('CREATE TABLE user(email text, password text)')

def create_user(email, password):
    con = sqlite3.connect('user2.db')
    c = con.cursor()
    c.execute("SELECT* FROM user WHERE email=:email AND password =:password",{'email':email, 'password':password})
    data = c.fetchone()
    if data == None:
        c.execute("INSERT INTO user (email,password) VALUES (?,?)", (email, password))
        con.commit()
        con.close()
        return 1
    else:
        con.close()
        return 2

def check_user(email, password):
    con = sqlite3.connect('user2.db')
    c = con.cursor()
    c.execute("SELECT* FROM user WHERE email=:email AND password =:password", {'email': email, 'password': password})
    data = c.fetchone()
    con.close()
    return data

test = check_user('sandra', 'äpple')
print(test)

conn.commit()

conn.close()
