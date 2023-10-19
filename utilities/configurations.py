import configparser
import mysql.connector
from mysql.connector import Error
import psycopg2

env = "DEV"

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

    
connect_config = {
    'user' : getConfig()[env]['DB_USER'],
    'password' : getConfig()[env]['DB_PASS'],
    'host' : getConfig()[env]['DB_HOST'],
    'database' :getConfig()[env]['DB_NAME'],
}

#For DB validation - to be impelemented
def getConnection():
    try:
        print(connect_config)
        conn = psycopg2.connect(**connect_config)
        if conn:
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

