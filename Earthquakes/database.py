import mysql.connector
from mysql.connector import errorcode

from settings import *

def connect_db():
    try:
        db = mysql.connector.connect(user=USER,
                                      password=PASSWORD,
                                      database=DB_NAME)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return db


def create_earthquakes_table():
    db = connect_db()
    cursor = db.cursor()

    create_table = (
        "CREATE TABLE IF NOT EXISTS `earthquakes` ("
        "   `id` int(11) NOT NULL AUTO_INCREMENT,"
        "   `date` date NOT NULL,"
        "   `location` varchar(100) NOT NULL,"
        "   `latitude` decimal(11,3) NOT NULL,"
        "   `longitude` decimal(11,3) NOT NULL,"
        "   `depth` decimal(11,3) NOT NULL,"
        "   `magnitude` decimal(11,3) NOT NULL,"
        "   PRIMARY KEY (`id`),"
        "   UNIQUE KEY `unique_index` (`date`, `location`, `depth`, `magnitude`)"
        ");"
    )

    cursor.execute(create_table)

    db.commit()
    cursor.close()
    db.close()


def save_earthquake_data(row_data):
    db = connect_db()
    cursor = db.cursor()

    add_earthquakes = (
        "INSERT INTO `earthquakes`"
        "(date, location, latitude, longitude, depth, magnitude)"
        "VALUES (%(date)s, %(place)s, %(lat)s, %(lon)s, %(depth)s, %(mag)s)"
        "ON DUPLICATE KEY UPDATE id=id"
        ";"
    )

    cursor.execute(add_earthquakes, row_data)

    db.commit()
    cursor.close()
    db.close()


def query_earthquake_data(magnitude):
    db = connect_db()
    cursor = db.cursor()

    query = ("SELECT location, magnitude, date FROM earthquakes "
             "WHERE magnitude >= " + str(magnitude))

    cursor.execute(query)

    for (location, magnitude, date) in cursor:
        print("{}: earthquake of magnitude {} on {}".format(
            location, magnitude, date))

    cursor.close()
    db.close()




def delete_data_table():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE earthquakes")
    db.close()
