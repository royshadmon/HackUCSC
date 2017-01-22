import csv
import datetime
import pprint
import time

import psycopg2

def main():
    connString = "host='envitedb.chsdj9v9ebik.us-west-1.rds.amazonaws.com' dbname='mydb' user='rshadmon' password='shadmon54321'"
    conn = psycopg2.connect(connString)

    # print the connection string we will use to connect
    print "Connecting to database\n	->%s" % (connString)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(connString)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Guests")
    records = cursor.fetchall()
    pprint.pprint(records)

    #print "Connected!\n"


    #choice = raw_input() # 'c' for csv or 'd' for card
    #choice = choice.upper()
    #if choice == 'C':
    #    csvFile()
    #elif choice == 'D':
    #    card()
    #else:
    #    main()


#if __name__ == "__main__":
#    main()



def card(ID):


    print "DROP TABLE IF EXISTS Guests;"
    print "CREATE TABLE Guests (" \
          "firstname char(30), " \
          "lastname char(30), " \
          "time_entered TIMESTAMP, " \
          "PRIMARY KEY(firstname, lastname));"
    #retrieveName = True
    #while retrieveName == True:
    scan = ID
    if scan == 'EXIT':
        exit()
    else:
        name = getName(scan)
        #if checkExists(name) == True:
         #   return "User has already entered"
        #else:
        parseName(name)


def csvFile():
    print "DROP TABLE IF EXISTS Guests;"
    print "CREATE TABLE Guests2 (" \
          "firstname char(30), " \
          "lastname char(30), " \
          "time_entered TIMESTAMP, " \
          "PRIMARY KEY(firstname, lastname));"
    with open('names.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            parseName(row)

def checkExists(name):
    print "SELECT " + name[0] + ", " +" FROM GUESTS "


def parseName(name):
    test = open('test.txt', 'w')

    ts = time.time()
    timestamp1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    test.write('INSERT INTO Guests VALUES(' + "'" + name[0] + "'" + ',' + "'" + name[1] + "'" + ',' + "'" + timestamp1 + "');")
    test.close()

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





if __name__ == "__main__": main()
