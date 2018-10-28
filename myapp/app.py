from flask import Flask
import mysql.connector 

app = Flask(__name__)

@app.route('/') 
def index():
    result = ''
    cnx = mysql.connector.connect(user='user1', password='pass1', host='example-mysql', database='db1')
    cursor = cnx.cursor()
    query = "SELECT name, address FROM contacts WHERE name=%s" 
    cursor.execute(query, ('Lee',))
    for (r_name, r_addr) in cursor:
        #result = "{} is living in {}".format(r_name, r_addr)
        result = "{} is living in {}. version 2".format(r_name, r_addr) 
    return result

if __name__ == '__main__': 
    app.run(host='0.0.0.0')