# Author: JingyiHui
# CSCI59000 Big Data Management
# 27 Oct 2018
# This code is implemented for the course project.
# In this part, the program map the csv data into correct form
# and insert it into database

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import date, datetime
import csv

count = 0
date_format = "%Y-%m-%d"
id_set = set()
# connect to database: BigDataDB on localhost
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="132052Hui",
        database="DemoDB"
        )
    mycursor = mydb.cursor()
    # load csv file
    with open('Demo_label.csv', 'r') as csvfile:
        csv_data = csv.reader(csvfile)
        # map each cell into correct data format
        next(csv_data)
        for row in csv_data:
            # print(count)
            # print(row)
            row[0] = int(row[0])
            if row[0] not in id_set:
                id_set.add(row[0])
                row[1] = float(row[1])
                row[2] = datetime.strptime(row[2], date_format).date()
                stat_values = ','.join(['%s'] * len(row))
                print('Inserting label:', str(count))
                mycursor.execute('INSERT INTO Demo_label VALUES (%s)' % stat_values, row)
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
