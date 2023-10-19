from utilities.configurations import *
import psycopg2
import psycopg2.extras

DB_HOST = getConfig()['SQL']['DB_HOST']
DB_NAME = getConfig()['SQL']['DB_NAME']
DB_USER = getConfig()['SQL']['DB_USER']
DB_PASS = getConfig()['SQL']['DB_PASS']


def getConnection():
    try :   
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

