import sqlite3
import pandas as pd


# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test.db')
# db_connect("PRAGMA foreign_keys = ON")
# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor
#CREATING TABLES
query = """
    CREATE TABLE Clinic(
    clinicNo INT CHECK(clinicNo>0),
    clinicName VARCHAR(100),
    address VARCHAR(100),
    phoneNum VARCHAR(10) CHECK(length(phoneNum)==10),
    managerStaffNo INT CHECK(managerStaffNo),
    PRIMARY KEY(clinicNo),
    FOREIGN KEY (managerStaffNo) REFERENCES staff(staffNo)
    ON DELETE CASCADE
    );
    """
cursor.execute(query)
query = """
 CREATE TABLE Owner(
    ownerNo  INT,
    name    VARCHAR(100),
    address VARCHAR(100),
    ownerPhone VARCHAR(10) CHECK(length(ownerPhone)=10),
    clinicNo INT,
    PRIMARY KEY(ownerNo),
    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    ON DELETE CASCADE
    );
"""
cursor.execute(query)
query = """
CREATE TABLE Staff(
staffNo INT,
clinicNo INT,
name VARCHAR(100),
address VARCHAR(100),
staffPhone VARCHAR(10) CHECK(length(staffPhone)=10),
DOB        VARCHAR(10) CHECK(DOB < "2004-01-01"),
position VARCHAR(100),
salary INT CHECK(salary>0),
PRIMARY KEY(staffNo),
FOREIGN KEY(clinicNo) REFERENCES Clinic(clinicNo)
ON DELETE CASCADE
);
"""
cursor.execute(query)
query = """
CREATE TABLE Pet(
petNo INT CHECK(petNo >0),
ownerNo INT,
clinicNo INT,
name VARCHAR(100),
DOB     VARCHAR (10),
species VARCHAR(100),
breed   VARCHAR(100),
color   VARCHAR(100),
PRIMARY KEY(petNo)
FOREIGN KEY(ownerNo) REFERENCES Owner(ownerNo),
FOREIGN KEY(clinicNo) REFERENCES Clinic(clinicNo)
ON DELETE CASCADE
);
""" 
cursor.execute(query)
query = """
CREATE TABLE Examination(
examNo INT CHECK(examNo >0),
chiefComplaint VARCHAR(100),
date   VARCHAR(10) CHECK(date <= "2022-12-08"),
actionTaken VARCHAR(100),
petNo INT CHECK(petNo >0),
staffNo INT CHECK(staffNo >0),
PRIMARY KEY(examNo)
FOREIGN KEY(petNo) REFERENCES Pet(petNo),
FOREIGN KEY(staffNo) REFERENCES staff(staffNo)
ON DELETE CASCADE
);
""" 
cursor.execute(query)
# Execute query, the result is stored in cursor


# Insert rows into the Clinic Table
query = """
    INSERT INTO Clinic (clinicNo,clinicName,address,phoneNum,managerStaffNo) 
    VALUES (62,"Barry Bonds Pet Care", "6253 Park Avenue","5615366410",31);
    """
cursor.execute(query)
query = """
INSERT INTO Clinic (clinicNo,clinicName,address,phoneNum,managerStaffNo) 
    VALUES (89,"Dr.G's Clinic for Critters", "1800 Martin Luther King Blvd","9542638957",NULL);
"""
cursor.execute(query)
query = """
INSERT INTO Clinic (clinicNo,clinicName,address,phoneNum,managerStaffNo) 
    VALUES (13,"Unlucky Pet Health Services", "96 Carlyle Rd","7623916578",56);
"""
cursor.execute(query)
query = """
INSERT INTO Clinic (clinicNo,clinicName,address,phoneNum,managerStaffNo) 
    VALUES (106,"South Side Veterinarian Center", "8971 Lake Shore Dr","9021013365",NULL);
"""
cursor.execute(query)
query = """
INSERT INTO Clinic (clinicNo,clinicName,address,phoneNum,managerStaffNo) 
    VALUES (33,"Adler Animal Hospital", "9856 San Marino Circle","3056650819",63);
"""
cursor.execute(query)
#Insert rows into Staff Table
query = """
INSERT INTO Staff(staffNo,clinicNo,name,address,staffPhone,DOB,position,salary) 
VALUES (56,13,"Benjamin Chodry", "56 Kimberly Estates",5506959506,1998-03-28,"Chief Technician",112000);
"""
cursor.execute(query)
query = """
INSERT INTO Staff(staffNo,clinicNo,name,address,staffPhone,DOB,position,salary) 
VALUES (63,33,"Dwayne Carter", "001 Holly Grove Street",4109505899,1982-09-27,"Veterinarian",260000);
"""
cursor.execute(query)
query = """
INSERT INTO Staff(staffNo,clinicNo,name,address,staffPhone,DOB,position,salary) 
VALUES (12,106,"Amy Greenberg", "22 Melrose Point",5286934578,2002-11-08,"Receptionist",16000);
"""
cursor.execute(query)
query = """
INSERT INTO Staff(staffNo,clinicNo,name,address,staffPhone,DOB,position,salary) 
VALUES (31,62,"Mike Chambers", "783 Palmetto Park Rd",8923672103,1976-06-15,"Office Manager",29500);
"""
cursor.execute(query)
query = """
INSERT INTO Staff(staffNo,clinicNo,name,address,staffPhone,DOB,position,salary) 
VALUES (115,89,"Jan Levinson", "21 Scranton Blvd",1569876521,1963-04-30,"Head Veterinarian",220000);
"""
cursor.execute(query)

# Insert rows into the Owner Table
query = """
INSERT INTO Owner(ownerNo,clinicNo,name,address,ownerPhone)
VALUES (233,106, "Kirsnick Ball", "52 Nawfside Rd", 9875623358);
"""
cursor.execute(query)
query = """
INSERT INTO Owner(ownerNo,clinicNo,name,address,ownerPhone)
VALUES (211,33, "John Snow", "6842 Hillside Lane", 5552106838);
"""
cursor.execute(query)
query = """
INSERT INTO Owner(ownerNo,clinicNo,name,address,ownerPhone)
VALUES (154,62, "Alena Gleeman", "2318 Mountain Hill Drive", 3736912387);
"""
cursor.execute(query)
query = """
INSERT INTO Owner(ownerNo,clinicNo,name,address,ownerPhone)
VALUES (93,89, "Rashida Bluestrike", "64 Cherry Red Rd", 1475623251);
"""
cursor.execute(query)
query = """
INSERT INTO Owner(ownerNo,clinicNo,name,address,ownerPhone)
VALUES (110,13, "Miguel Gonzalez", "1165 Oceanic Plaza", 2326587769);
"""
cursor.execute(query)


#Insert into Pet
query = """
INSERT INTO Pet(petNo,name,DOB,species,breed,color,ownerNo,clinicNo)
VALUES (1164, "Rex","2016-03-14","dog","pitbull","brown",233,106);
"""
cursor.execute(query)
query = """
INSERT INTO Pet(petNo,name,DOB,species,breed,color,ownerNo,clinicNo)
VALUES (1258,"Domino","2022-02-10","dog","dalmation","white",211,33);
"""
cursor.execute(query);
query = """
INSERT INTO Pet(petNo,name,DOB,species,breed,color,ownerNo,clinicNo)
VALUES (958, "Timothy","2018-10-06","parrot","macaw","green",211,33);
"""
cursor.execute(query)
query = """
INSERT INTO Pet(petNo,name,DOB,species,breed,color,ownerNo,clinicNo)
VALUES (753, "Cristoff","2017-01-19","cat","shorthair","grey",154,62);
"""
cursor.execute(query)
query = """
INSERT INTO Pet(petNo,name,DOB,species,breed,color,ownerNo,clinicNo)
VALUES (432, "Kobe","2019-05-26","snake","mamba","black",93,89);
"""
cursor.execute(query);
#Insert values into Examination table
query = """
INSERT INTO Examination(examNo,chiefComplaint,date,actionTaken,petNo,staffNo)
VALUES(3651,"Broken Bone","2022-12-05","Metal screw inserted",1164,115);
"""
cursor.execute(query)
query = """
INSERT INTO Examination(examNo,chiefComplaint,date,actionTaken,petNo,staffNo)
VALUES(2193,"Broken Bone","2019-03-20","Surgery",1258,63);
"""
cursor.execute(query)
query = """
INSERT INTO Examination(examNo,chiefComplaint,date,actionTaken,petNo,staffNo)
VALUES(1967,"Broken Bone","2018-11-30","Metal plate inserted",753,56);
"""
cursor.execute(query)
query = """
INSERT INTO Examination(examNo,chiefComplaint,date,actionTaken,petNo,staffNo)
VALUES(3111,"Avian Flu","2022-11-18","Perscribed antibiotics",958,63);
"""
cursor.execute(query)
query = """
INSERT INTO Examination(examNo,chiefComplaint,date,actionTaken,petNo,staffNo)
VALUES(2831,"Parasitic infection","2021-08-30","De-worming injection given",432,115);
"""
cursor.execute(query)

# 5 SQL Queries are below

#QUERY 1: What are the StaffNo, names, and positions of staff members who earn more than $30,000 a year
query = """
    SELECT staffNo, name, position
    FROM Staff
    WHERE salary > 30000
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)


#QUERY 2: How many pets does the owner with the ownerNo 211 have?
query = """
SELECT count(petNo)as numOfPets
FROM Owner o, Pet p
WHERE p.ownerNo = o.ownerNo AND p.ownerNo = 211
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

#QUERY 3: What are the clinic numbers and names of clinic with no staff members as managers?
query = """
SELECT c.clinicNo,c.clinicName
FROM Clinic c
WHERE c.managerStaffNo IS NULL
"""
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)


#QUERY 4: What are the names of pets that were examined for a broken bone?
query = """
SELECT p.name
FROM Pet p, Examination e
WHERE e.petNo = p.petNo AND e.chiefComplaint = "Broken Bone"
"""
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)


#QUERY 5: How many examinations were performed on 11/18/2022?
query = """
SELECT count(examNo) numOfExams
FROM Examination
WHERE date = "2022-11-18"
"""
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)




# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
