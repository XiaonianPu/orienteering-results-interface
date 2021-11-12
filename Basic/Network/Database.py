from os import environ

import fdb
import pymysql
IS_MYSQL=False
IS_FIREBIRD=True

DB = None
# if environ["DB_REMOTE"] == 1:
if False:
    if environ["DB_TYPE"] == "MYSQL":
        DB = pymysql.connect(user=environ["DB_USER"], password=environ["DB_PASSWORD"], host=environ["DB_HOST"],
                             database=environ["DB_DATABASE"])
    else:
        DB = fdb.connect(dsn=environ["DB_HOST"]+":"+environ["DB_DATABASE"], password=environ["DB_PASSWORD"], user=environ["DB_USER"])
    DB.close()


def connect():
    global DB
    if DB.closed:
        DB = fdb.connect(charset="UTF8",dsn=environ["DB_HOST"]+":"+environ["DB_DATABASE"], password=environ["DB_PASSWORD"], user=environ["DB_USER"])
    return DB, DB.cursor()


def close():
    global DB
    if not DB.closed:
        DB.close()

