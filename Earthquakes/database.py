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
        "   `location` varchar(40) NOT NULL,"
        "   `latitude` decimal(5,3) NOT NULL,"
        "   `longitude` decimal(5,3) NOT NULL,"
        "   `depth` decimal(5,3) NOT NULL,"
        "   `magnitude` decimal(5,3) NOT NULL,"
        "   PRIMARY KEY (`id`),"
        "   UNIQUE KEY `unique_index` (`date`, `location`)"
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
        "(location, latitude, longitude, depth, magnitude)"
        "VALUES (%(place)s, %(lat)s, %(lon)s, %(depth)s, %(mag)s)"
    )

    cursor.execute(add_earthquakes, row_data)

    db.commit()
    cursor.close()
    db.close()


def delete_data_table():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE earthquakes")
    db.close()
