import pymysql
import json
import pandas as pd

class SQLdata:
    def __init__(self, dataFrame) -> None:
        self.df = dataFrame

        # getting the mysql credentials
        with open ('MySQL_DB_Details.json', 'r') as fp:
            data = json.load(fp)

        self.hostName = data[0]['hostname']
        self.userName = data[0]['username']
        self.passWord = data[0]['password']
        self.dbName = data[0]['databaseName']
        self.tbName = data[0]['tableName']

    def createDatabase(self):
        """ Method for creating the database inside mysql server. """
        connection = pymysql.connect(
            host = self.hostName,      # ip address of Mysql server
            user = self.userName,      # username
            password = self.passWord   # password
        )

        db_query = 'CREATE DATABASE IF NOT EXISTS {}'.format(self.dbName)
        cursor = connection.cursor()
        cursor.execute(db_query)
        cursor.close()
        connection.close()
    
    def createTable(self):
        """ Method for creating the table inside the created database. """
        connection = pymysql.connect(
            host = self.hostName,      # ip address of Mysql server
            user = self.userName,      # username
            password = self.passWord,  # password
            db = self.dbName
        ) 

        create_table_query = " CREATE TABLE IF NOT EXISTS {} (Name VARCHAR(200), Title VARCHAR(200), Gender VARCHAR(200), Expertise TEXT, Research TEXT, Phone VARCHAR(100), Location TEXT, Education TEXT)".format(self.tbName)

        cursor = connection.cursor()
        cursor.execute(create_table_query)

        connection.commit()
        cursor.close()
        connection.close()

    def insertRecordsDf(self):
        """ Method for inserting records into mysql database. """
        for _, row in self.df.iterrows():
            connection = pymysql.connect (
                host = self.hostName,      # ip address of Mysql server
                user = self.userName,      # username
                password = self.passWord,  # password
                db = self.dbName
            )
            cursor = connection.cursor()
            sql = "INSERT INTO {} (Name, Title, Gender, Expertise, Research, Phone, Location, Education) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(self.tbName)

            # Execute the query
            cursor.execute(sql, (row['Name'], row['Title'], row['Gender'], row['Expertise'], row['Research_Interests'], row['Phone'], row['Location'], row['Education']))
            cursor.close()
            connection.commit()
            connection.close()
