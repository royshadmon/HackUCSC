DROP TABLE IF EXISTS Guests;
CREATE TABLE Guests (firstname char(30), lastname char(30), time_entered TIMESTAMP, PRIMARY KEY(firstname, lastname));
INSERT INTO Guests VALUES('ALON','PEKUROVSKY','2017-01-21 03:54:39');
INSERT INTO Guests VALUES('ROY','SHADMON','2017-01-21 03:54:42');
