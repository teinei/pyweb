import sqlite3
import time
from numpy import genfromtxt

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def Create_DB(db):      
    #Create DB and format it as needed
    with sqlite3.connect(db) as conn:
        conn.row_factory = dict_factory
        conn.text_factory = str

        cursor = conn.cursor()

        cursor.execute("CREATE TABLE [Price_History] ([id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, [date] DATE, [opn] FLOAT, [hi] FLOAT, [lo] FLOAT, [close] FLOAT, [vol] INTEGER);")


def Add_Record(db, data):
    #Insert record into table
    with sqlite3.connect(db) as conn:
        conn.row_factory = dict_factory
        conn.text_factory = str

        cursor = conn.cursor()

        cursor.execute("INSERT INTO Price_History({cols}) VALUES({vals});".format(cols = str(data.keys()).strip('[]'), 
                    vals=str([data[i] for i in data]).strip('[]')
                    ))


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skiprows=1, converters={0: lambda s: str(s)})
    return data.tolist()


if __name__ == "__main__":
    t = time.time() 

    db = 'csv_test_sql.db' #Database filename 
    file_name = "t.csv" #sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv

    data = Load_Data(file_name) #Get data from CSV

    Create_DB(db) #Create DB

    #For every record, format and insert to table
    for i in data:
        record = {
                'date' : i[0],
                'opn' : i[1],
                'hi' : i[2],
                'lo' : i[3],
                'close' : i[4],
                'vol' : i[5]
            }
        Add_Record(db, record)

    print "Time elapsed: " + str(time.time() - t) + " s." #3.604s