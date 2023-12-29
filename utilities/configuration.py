import os, configparser, allure
import psycopg2

env = "USM"

def getConfig():
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), 'properties.ini')
    if config.read(config_file): 
        return config
    else:
        raise FileNotFoundError("Config file 'utilities/properties.ini' not found or empty.")
    
def add_allure_step(description):
    with allure.step(description):
        pass