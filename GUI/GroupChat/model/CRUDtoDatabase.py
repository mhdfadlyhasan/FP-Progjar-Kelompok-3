import mysql.connector
from dotenv import load_dotenv
load_dotenv()
# OR, the same with increased verbosity
load_dotenv(verbose=True)
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
import os

class dbHelper:
    def __init__(self):
        self.server_connect = mysql.connector.connect(
            host="localhost",
            user=os.getenv("DB_USERNAME"),
            passwd=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
    def select_from(self,column_name, table_name, where):
        if(not where):
            where='true'
        cursor = self.server_connect.cursor()
        cursor.execute("select {} from {} where {}".format(column_name,table_name,where))
        row = cursor.fetchall()
        if row:
            return row
        else:
            return None
    def insert_into(self,table_name, column_name, values):
        cursor = self.server_connect.cursor()
        cursor.execute("insert into {}({}) values ({})".format(table_name,column_name,values))
        self.server_connect.commit()

    def delete(self,table_name, where):
        cursor = self.server_connect.cursor()
        cursor.execute("Delete from {} where {}".format(table_name,where))
        self.server_connect.commit()
        
