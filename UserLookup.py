import sqlite3

# Look up users phone number by name
@app.route('/user/<username>', methods=['GET'])

def lookUp(name):
    cur.execute('SELECT phoneNum FROM USERS WHERE' + name + ';')
