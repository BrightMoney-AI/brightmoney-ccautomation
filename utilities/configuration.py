import os, configparser, json
import psycopg2

env = "DEV"

def getConfig():
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), 'properties.ini')
    if config.read(config_file): 
        return config
    else:
        raise FileNotFoundError("Config file 'utilities/properties.ini' not found or empty.")
    
connect_config = {
    'user' : getConfig()[env]['DB_USER'],
    'password' : getConfig()[env]['DB_PASS'],
    'host' : getConfig()[env]['DB_HOST'],
    'database' :getConfig()[env]['DB_NAME'],
}

def getConnection():
    try:
        print(connect_config)
        conn = psycopg2.connect(**connect_config)
        if conn:
            print("Connection Successful")
            return conn
    except Exception as e:
        print(e)