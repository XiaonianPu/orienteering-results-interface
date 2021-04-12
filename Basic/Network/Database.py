from os import environ

import pymysql

if environ["DB_REMOTE"] is True:
    DB = pymysql.connect(user=environ["DB_USER"], password=environ["DB_PASSWORD"], host=environ["DB_HOST"],
                         database=environ["DB_DATABASE"])
    DB.close()
else:
    DB = None


def connect():
    if not DB.open:
        DB.connect()
    return DB, DB.cursor()


def close():
    if DB.open:
        DB.close()

