import csv
import datetime
import time

def main():

    choice = raw_input() # 'c' for csv or 'd' for card
    choice = choice.upper()
    if choice == 'C':
        csvFile()
    elif choice == 'D':
        card()
    else:
        main()

def card():
    print "DROP TABLE IF EXISTS Guests;"
    print "CREATE TABLE Guests (" \
          "firstname char(30), " \
          "lastname char(30), " \
          "time_entered TIMESTAMP, " \
          "PRIMARY KEY(firstname, lastname));"
    retrieveName = True
    while retrieveName == True:
        scan = raw_input()
        scan = scan.upper()
        if scan == 'EXIT':
            break
        else:
            name = getName(scan)
            if checkExists(name) == True
                return "User has already entered"
            else:
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
    ts = time.time()
    timestamp1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print ('INSERT INTO Guests VALUES(' + "'" + name[0] + "'" + ',' + "'" + name[1] + "'" + ',' + "'" + timestamp1 + "');")

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
