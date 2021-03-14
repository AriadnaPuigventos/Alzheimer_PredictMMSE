# Needed for stablishing connection with database and queries
import json
import pymysql
import psycopg2
from sqlalchemy import create_engine
import sys

# For data export as csv and/or dataframe
import pandas as pd

class General_SQL (object):
    def __init__(self, path):
        self.path = path


    # For reading config files
    def read_config(self):
        """
                            ---What it does---
        Loads a json file and turns it into a dictionary.
                            
                            ---What it needs---
            - The path to the file (path) in string format
        
                            ---What it returns---
        A dictionary (settings) with the contents of the json loaded
        """
        try:
            with open(self.path, 'r+') as outfile:
                self.settings = json.load(outfile)
                              
                return self.settings
            
        except Exception as error:
            raise ValueError(error)


    # For connecting your Database
    def CREATE_a_MySQL_db(self):

        try:             
            self.settings = self.settings['Cloud']

            IP_DNS = self.settings["IP_DNS"]
            USER = self.settings["USER"]
            PASSWORD = self.settings["PASSWORD"]
            DATABASE = self.settings["DB_NAME"]
            PORT = self.settings["PORT"]

            self.connection = pymysql.connect(host= IP_DNS, user= USER, 
                                    password= PASSWORD, database= DATABASE, 
                                    port= PORT)
            
            self.cursor = self.connection.cursor()
                     
            print(f"Connected to MySQL server {DATABASE}")
                                            
            return self.connection, self.cursor
       
        except Exception as error:
            raise ValueError(error)        
