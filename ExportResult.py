# Author: JingyiHui
# CSCI59000 Big Data Management
# 15 Oct 2018
# This code is implemented for the course project.
# In this part, the program fetch the result from queries
# and export it into a csv file

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import csv

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="132052Hui",
        database="DemoDB"
        )
mycursor = mydb.cursor()

# query 1: get the joined data for training
mycursor.execute("SELECT * FROM Demo_property INNER JOIN Demo_label ON Demo_property.parcelid = Demo_label.parcelid")
result_1 = mycursor.fetchall()
csvfile = open('Demo_Query_1.csv', 'w')
myfile = csv.writer(csvfile)
myfile.writerows(result_1)
csvfile.close()
print('Query 1 Result Exported...')

# query 2: geo distribution of the properties sold and its average log error
mycursor.execute("SELECT regionidcity, COUNT(regionidcity)AS city_count, AVG(logerror) AS avg_error "
                 "FROM Demo_property INNER JOIN Demo_label "
                 "ON Demo_property.parcelid = Demo_label.parcelid "
                 "WHERE regionidcity IS NOT NULL "
                 "GROUP BY regionidcity "
                 "ORDER BY city_count")
result_2 = mycursor.fetchall()
csvfile = open('Demo_Query_2.csv', 'w')
myfile = csv.writer(csvfile)
myfile.writerows(result_2)
csvfile.close()
print('Query 2 Result Exported...')

# query 3: get the average log error grouped by each year
mycursor.execute("SELECT yearbuilt, AVG(logerror)  AS avgerror "
                 "FROM Demo_property INNER JOIN Demo_label "
                 "ON Demo_property.parcelid = Demo_label.parcelid "
                 "WHERE yearbuilt IS NOT NULL "
                 "GROUP BY yearbuilt "
                 "ORDER BY yearbuilt;")
result_3 = mycursor.fetchall()
csvfile = open('Demo_Query_3.csv', 'w')
myfile = csv.writer(csvfile)
myfile.writerows(result_3)
csvfile.close()
print('Query 3 Result Exported...')

# query 4: get the distribution of property value and log error
mycursor.execute("SELECT taxamount, logerror "
                 "FROM Demo_property INNER JOIN Demo_label "
                 "ON Demo_property.parcelid = Demo_label.parcelid")
result_4 = mycursor.fetchall()
csvfile = open('Demo_Query_4.csv', 'w')
myfile = csv.writer(csvfile)
myfile.writerows(result_4)
csvfile.close()
print('Query 4 Result Exported...')
