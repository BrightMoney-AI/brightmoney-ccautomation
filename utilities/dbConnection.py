import psycopg2
from utilities.configuration import *

def getConnection():
    try:
        print(connect_config)
        conn = psycopg2.connect(**connect_config)
        if conn:
            print("Connection Successful")
            return conn
    except Exception as e:
        print(e)