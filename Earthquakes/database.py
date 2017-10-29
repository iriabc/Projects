import mysql.connector
from mysql.connector import errorcode

from settings import *

def connectDb():
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


def saveEarthquakeData(row_data, data_type):
    if data_type == 'EARTHQUAKES':
        DB_TABLE = 'all_earthquakes'
    elif data_type == 'BIG_EARTHQUAKES':
        DB_TABLE = 'big_earthquakes'

    db = connectDb()
    cursor = db.cursor()

    add_earthquakes = ("INSERT INTO " + DB_TABLE + " "
                    "(location, latitude, longitude, depth, magnitude)"
                    "VALUES (%(place)s, %(lat)s, %(lon)s, %(depth)s, %(mag)s)")

    cursor.execute(add_earthquakes, row_data)

    db.commit()
    cursor.close()
    db.close()


def deleteDataTable():
    db = connectDb()
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE all_earthquakes")
    cursor.execute("TRUNCATE TABLE big_earthquakes")
    db.close()