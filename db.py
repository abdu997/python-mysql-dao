import mysql.connector
import json
from config import MYSQL

mydb = mysql.connector.connect(
    host= MYSQL['host'],
    user=MYSQL['user'],
    passwd=MYSQL['passwd'],
    database=MYSQL['database']
)

def execute(query, values=None):
    if values == None:
        mydb.cursor().execute(query)
    else:
        mydb.cursor().execute(query, values)
    mydb.commit()
    return mycursor

def executemany(query, values=None):
    if values == None:
        mydb.cursor().executemany(query)
    else:
        mydb.cursor().executemany(query, values)
    mydb.commit()
    return mycursor

def fetchall(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    columns = [col[0] for col in mycursor.description]
    rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]
    return rows

def fetchone(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    columns = [col[0] for col in mycursor.description]
    result = {}
    for i, col in enumerate(columns):
        result[col] = mycursor.fetchone()[i]
    return result
