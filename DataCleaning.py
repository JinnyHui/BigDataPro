# Author: JingyiHui
# CSCI59000 Big Data Management
# 22 Oct 2018
# This code is implemented for the course project.
# In this part, the program clean the unformatted data
# and output the clean data into a new csv file

import pandas as pd


def data_info(datafile, outfile):
    """
    get the basic information of our dataset
    :param datafile: the input dataset in dataframe
    :param outfile: the output report file
    :return: None
    """
    row, column = datafile.shape
    # write the shape of dataset
    outfile.write('\n' + separator)
    outfile.write('\nThe dataset contains:' + str(row) + ' instances, and ' + str(column) + ' attributes.')
    print(separator)
    print('The dataset contains:' + str(row) + ' instances, and ' + str(column) + ' attributes.')
    print(separator, '\n')
    outfile.write('\n' + separator + '\n')
    # datafile.head().to_csv('Describe.csv', sep=',')
    datafile.describe().to_csv('Report_2.csv', sep=',')
    print('Data info:')
    print(datafile.describe())


def data_clean(datafile):
    """
    delete useless attributes, get data formatted
    :param datafile:
    :return: cleaned dataset
    """
    # delete the geometry data
    dataset_new = datafile.drop(['latitude', 'longitude'], axis=1)
    row_no, column_no = dataset_new.shape
    for i in range(row_no):
        print('Checking data instance:', str(i))
        # turn TRUE into 1 in column 'hashottuborspa'
        cell_value1 = dataset_new.iloc[i]['hashottuborspa']
        if type(cell_value1) == bool and cell_value1 is True:
            # print(cell_value1, type(cell_value1))
            dataset_new.set_value(i, 'hashottuborspa', 1)

        # turn Y into 1 in column 'taxdelinquencyflag'
        cell_value2 = dataset_new.iloc[i]['taxdelinquencyflag']
        if cell_value2 == 'Y':
            dataset_new.set_value(i, 'taxdelinquencyflag', 1)

        # turn 2 digits number into 4 digits number in column 'taxdelinquencyyear'
        cell_value3 = dataset_new.iloc[i]['taxdelinquencyyear']
        if cell_value3 > 0:
            new_value = int(int(cell_value3) + 2000)
            dataset_new.set_value(i, 'taxdelinquencyyear', new_value)
    return dataset_new


if __name__ == '__main__':
    separator = '################################################################################'
    filename = 'Report_1.txt'
    output = open(filename, 'w')
    df = pd.read_csv('Demo.csv')
    data_info(df, output)
    cleaned_data = data_clean(df)
    cleaned_data.to_csv("Demo_clean.csv", sep=',', index=False)
    print("Done!")
