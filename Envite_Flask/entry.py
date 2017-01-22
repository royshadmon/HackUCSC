import csv
import ctypes
import datetime
import pprint
import time
import psycopg2
from flask import redirect
from flask import url_for


import Envite_Flask
from flask import Flask, flash, render_template

from flask import render_template

def main():

    connectionString = 'dbname=mydb user=rshadmon password=shadmon54321 host=envitedb.chsdj9v9ebik.us-west-1.rds.amazonaws.com'
    try:
        conn = psycopg2.connect(connectionString)
        print "Connected"

    except:
        print "Unable to connect to the database"

    cur = conn.cursor()
    #createTable(cur, conn) #creates table
    #csvInsert(cur, conn)     #input into database
    Envite_Flask.main()




def createTable(cur, conn):
    try:
        cur.execute('CREATE TABLE test11(firstname char(30), lastname char(30), time_entered TIMESTAMP DEFAULT SET NULL);')
        print "table made"
        conn.commit()

    except:
        print "I can't creat the test table!"

def csvInsert(cur, conn):
    with open('names.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            statement = parseName(row)
            cur.execute(statement)
            conn.commit()
    csvfile.close()
    conn.close()


def parseName(row):
    #add on html another form
    test = open('test.txt', 'w')


    print "INSERT INTO Guests VALUES(' + "'" + row[0] + "'" + ',' + "'" + row[1] + "'" + ' );"
    return 'INSERT INTO Guests VALUES(' + "'" + row[0] + "'" + ',' + "'" + row[1] + "'" + ',' + "'" "');"



def cardSwipe(ID):
    name = getName(ID)
    print "end cardswipe "
    checkExists(name)




def checkExists(name):
    ts = time.time()
    timestamp1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    error = None
    connectionString = 'dbname=mydb user=rshadmon password=shadmon54321 host=envitedb.chsdj9v9ebik.us-west-1.rds.amazonaws.com'
    #"SELECT * FROM guests WHERE firstname='" + name[0] + "' AND lastname='" + name[1] + "';"
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
    print name[0] + "      " + name[1]
    #print "SELECT * FROM guests WHERE firstname='" + name[0] + "' AND lastname='" + name[1] + "';"
    cur.execute("SELECT * FROM guests WHERE firstname='" + name[0] + "' AND lastname='" + name[1] + "';")
    conn.commit()
    result = cur.fetchone()
    print "result = " + str(result)
    print type(result)
    if result is None:
        #flash("Person not in system")
        #return redirect(url_for('index'))
        #ctypes.cdll.user32.MessageBoxW(0, "Guest not in system", "WARNING", 1)
        print "Guest not in system"
    else:
        updateStatement = "UPDATE guests SET time_entered = '%s' WHERE firstname = '%s' AND lastname = '%s';" %(timestamp1,name[0],name[1])
        print updateStatement
        cur.execute(updateStatement)
        conn.commit()




def getName(licenseScan):
    #Parse a driver's license for First and last name

    #initialize the list
    name = []

    #licenseScan = str(raw_input())

    indKarat1 = licenseScan.find("^") #Find first ^

    #find the first $ sign
    indDol1 = licenseScan.find("$") #Find first $


    lastName = licenseScan[indKarat1 + 1: indDol1]

    #find next ^ sign, if there is a $ before it then theres a
    #middle name

    indKarat2 = licenseScan.find("^", indDol1) #Find second ^
    indDol2 = licenseScan.find("$", indDol1 + 1) #Find second $

    #if there is a second $ before the second ^ then theres a middle name

    if indDol2 != -1:
        firstName = licenseScan[indDol1 + 1: indDol2]
        #middleName = licenseScan[indDol2 + 1: indKarat2]
        #print(middleName)
        name.append(firstName)
        name.append(lastName)
        return name

    else:
        firstName = licenseScan[indDol1 + 1 : indKarat2]
        name.append(firstName)
        name.append(lastName)
        return name

if __name__ == "__main__":
    main()





            # cursor1 = conn.cursor()

# cursor1.execute("SELECT * FROM guests")
# cursor1.commit()
# results = cursor1.fetchall()
# print results

# conn = "host='envitedb.chsdj9v9ebik.us-west-1.rds.amazonaws.com' dbname='mydb' user='rshadmon' password='shadmon54321'"
##conn = psycopg2.connect(connString)

# print the connection string we will use to connect
# print "Connecting to database\n	->%s" % (connString)

# get a connection, if a connect cannot be made an exception will be raised here
# conn = psycopg2.connect(connString)

# conn.cursor will return a cursor object, you can use this cursor to perform queries

# cursor1.execute("SELECT * FROM Guests")
# records = cursor1.fetchall()
# pprint.pprint(records)

# print "Connected!\n"


# choice = raw_input() # 'c' for csv or 'd' for card
# choice = choice.upper()
# if choice == 'C':
#    csvFile()
# elif choice == 'D':
#    card()
# else:
#    main()

