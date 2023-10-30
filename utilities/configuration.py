import os, configparser, allure
import psycopg2

env = "DEV"

def getConfig():
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), 'properties.ini')
    if config.read(config_file): 
        return config
    else:
        raise FileNotFoundError("Config file 'utilities/properties.ini' not found or empty.")
    


# def getConnection():
#     try:
#         #print(connect_config)
#         conn = psycopg2.connect(**connect_config)
#         if conn:
#             with allure.step("DB Connection Successful"):
#                 print("DB Connection Successful")
#                 return conn
#     except Exception as e:
#         print(e)