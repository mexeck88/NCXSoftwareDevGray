@app.route('/users/<name>', methods=['DELETE'])
def del(name):
    cur.execute('DELETE FROM USERS WHERE' + name + ";" )
