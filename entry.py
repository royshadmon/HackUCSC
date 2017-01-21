import csv

def main():
    with open('names.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            parseName(row)


def parseName(name):
    print "INSERT INTO TABLE Guests VALUES(", name[0] , "," , name[1],");"




if __name__ == "__main__": main()