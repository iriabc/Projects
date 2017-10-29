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


def save_earthquake_data(row_data, data_type):
    if data_type == 'EARTHQUAKES':
        DB_TABLE = 'all_earthquakes'
    elif data_type == 'BIG_EARTHQUAKES':
        DB_TABLE = 'big_earthquakes'

    db = connect_db()
    cursor = db.cursor()

    add_earthquakes = ("INSERT INTO " + DB_TABLE + " "
                    "(location, latitude, longitude, depth, magnitude)"
                    "VALUES (%(place)s, %(lat)s, %(lon)s, %(depth)s, %(mag)s)")

    cursor.execute(add_earthquakes, row_data)

    db.commit()
    cursor.close()
    db.close()


def delete_data_table():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE all_earthquakes")
    cursor.execute("TRUNCATE TABLE big_earthquakes")
    db.close()