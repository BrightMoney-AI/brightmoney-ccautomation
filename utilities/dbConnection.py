import psycopg2
from utilities.configuration import *

base_connect_config = {
    'user' : getConfig()[env]['DB_USER'],
    'password' : getConfig()[env]['DB_PASS'],
    'host' : getConfig()[env]['DB_HOST'],  
}

def create_connection_config(dynamic_db_name):
    if dynamic_db_name == 'usm':
        database_name = 'DB_NAME'
    elif dynamic_db_name == 'payments':
        database_name = 'PAYMENTS_DB_NAME'
    return {**base_connect_config, 'database' :getConfig()[env][database_name]}


def getConnection(dynamic_db_name):
    try:
        connect_config = create_connection_config(dynamic_db_name)
        conn = psycopg2.connect(**connect_config)
        if conn:
            with allure.step("DB Connection Successful"):
                return conn
    except Exception as e:
        add_allure_step(str(e))