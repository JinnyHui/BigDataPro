# Author: JingyiHui
# CSCI59000 Big Data Management
# 15 Oct 2018
# This code is implemented for the course project.
# In this part, the program map the csv data into correct form
# and insert it into database

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import date, datetime
import csv

count = 0
# connect to database: BigDataDB on localhost
try:
    # connect to the local server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="132052Hui",
        database="DemoDB"
    )

    # print all the tables in the database if any
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for i in mycursor:
        print(i)

    # load the cleaned data into database
    with open('Demo_clean.csv', 'r') as csvfile:
        decimal_list = [3, 4, 52]
        varchar_list = [30, 32, 33]
        csv_data = csv.reader(csvfile)
        # map each cell into correct data format
        next(csv_data)
        for row in csv_data:
            print('Inserting property ID:', row[0])
            for i in range(len(row)):
                if i == 37:
                    row[i] = str(int(float(row[i]))) if row[i] else None
                if i == 47:
                    row[i] = 1 if row[i] == 'TRUE' else None
                if i == 55:
                    row[i] = str(int(float(row[i]))) if row[i] else None
                if i in decimal_list:
                    row[i] = float(row[i]) if row[i] else None
                elif i in varchar_list:
                    row[i] = str(row[i]) if row[i] else None
                else:
                    row[i] = int(float(row[i])) if row[i] else None
            # print(row)
            stat_values = ','.join(['%s'] * len(row))
            # print(stat_values)
            mycursor.execute('INSERT INTO Demo_property VALUES (%s)' % stat_values, row)
            count += 1
        mydb.commit()

except mysql.connector.Error as error:
    mydb.rollback()  # rollback if any exception occurred
    print("Failed inserting record into table".format(error))

finally:
    # closing database connection.
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")
