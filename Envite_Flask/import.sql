CREATE TABLE Guests (
          firstname char(30),
          lastname char(30),
          time_entered TIMESTAMP,
          PRIMARY KEY(firstname, lastname)
);


\copy Guests FROM "/Users/alonpek/Documents/Hackathon/HackUCSC/names.csv" DELIMITER ',' CSV HEADER;

SELECT *
FROM  Guests
