# QUESTION 1:
# Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors

import MySQLdb
db = MySQLdb.connect('localhost', 'root', 'newrootpassword', 'assigndb')
cursor = db.cursor()


sql1 = """CREATE TABLE BOOKS( 
          BOOK_ID INT NOT NULL,
          TITLE_ID INT)"""

sql2 = """CREATE TABLE TITLES( 
          TITLE_ID INT NOT NULL,
          TITLE CHAR(30), 
          PUBLISHER_ID INT,
          PUBLICATION_YEAR INT) """

sql3 = """CREATE TABLE PUBLISHERS(
          PUBLISHER_ID INT NOT NULL,
          NAME CHAR(30),
          ADDRESS CHAR(30),
          ZIP_CODE_ID INT) """


sql4 = """CREATE TABLE ZIP_CODES(
          ZIP_CODE_ID INT NOT NULL,
          CITY CHAR(20),
          STATE CHAR(20),
          ZIP_CODE INT)"""


sql5 = """CREATE TABLE AUTHORS_TITLES(
          AUTHOR_TITLE_ID INT NOT NULL,
          AUTHOR_ID INT,
          TITLE_ID INT)"""


sql6 = """CREATE TABLE AUTHORS(
          AUTHOR_ID INT NOT NULL,
          FIRST_NAME CHAR(10),
          MIDDLE_NAME CHAR(10),
          LAST_NAME CHAR(10))"""
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)


# QUESTION 2:
# Insert values in the tables.

insert1 = """INSERT INTO BOOKS(BOOK_ID,TITLE_ID) 
             VALUES(122, 22)"""
try:
    cursor.execute(insert1)
    db.commit()
except:
    db.rollback()

insert2 = """INSERT INTO TITLES( TITLE_ID,TITLE,PUBLISHER_ID,PUBLICATION_YEAR ) 
             VALUES(122,"COOL PYTHON",208,2019)"""
try:
    cursor.execute(insert2)
    db.commit()
except:
    db.rollback()

insert3 = """INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,ADDRESS,ZIP_CODE_ID ) 
             VALUES(208,"PEARSON","NOIDA",1)"""
try:
    cursor.execute(insert3)
    db.commit()
except:
    db.rollback()

insert4 = """INSERT INTO ZIP_CODES(ZIP_CODE_ID,CITY,STATE,ZIP_CODE) 
             VALUES(1,"YAMUNANAGAR","HARYANA",214002)"""
try:
    cursor.execute(insert4)
    db.commit()
except:
    db.rollback()

insert5 = """INSERT INTO AUTHORS_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID ) 
             VALUES(100,101,285)"""
try:
    cursor.execute(insert5)
    db.commit()
except:
    db.rollback()

insert6 = """INSERT INTO AUTHORS(AUTHOR_ID, FIRST_NAME, MIDDLE_NAME,LAST_NAME ) 
             VALUES(101,"MAYANK"," ","KUMAR")"""
try:
    cursor.execute(insert6)
    db.commit()
except:
    db.rollback()


# QUESTION 3:
# Update any values in any of the tables. Print the original and updated values.

upd = """UPDATE TITLES SET TITLE="PYTHON TRICKS" 
         WHERE PUBLISHER_ID=208"""
sq = "SELECT * FROM TITLE WHERE PUBLISHER_ID = 208"
try:
    """
    Printing values before updating
    """
    cursor.execute(sq)
    result = cursor.fetchall()
    for rows in result:
        title_id = rows[0]
        title = rows[1]
        publisher_id = rows[2]
        publication_year = rows[3]
        print("title_id", title_id, "title", title, "publisher_id", publisher_id, "publication_year", publication_year)

    cursor.execute(upd)
    """
    Printing values after updating
    """
    cursor.execute(sq)
    result = cursor.fetchall()
    for rows in result:
        title_id = rows[0]
        title = rows[1]
        publisher_id = rows[2]
        publication_year = rows[3]
        print("title_id", title_id, "title", title, "publisher_id", publisher_id, "publication_year", publication_year)

    db.commit()
except:
    db.rollback()
    print("Error occurred!")

db.close()


# Finally done.

print("\n\nDone")
