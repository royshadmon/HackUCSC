#Parse a driver's license for First and last name

licenseScan = str(raw_input())

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
    middleName = licenseScan[indDol2 + 1: indKarat2]
    print(firstName)
    print(middleName)
    print(lastName)

else:
    firstName = licenseScan[indDol1 + 1 : indKarat2]
    print (firstName)
    print (lastName)


