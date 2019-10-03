# Author: JingyiHui
# CSCI59000 Big Data Management
# 5 Dec 2018
# This code is implemented for the course project.
# In this script, the processes of Relational Database part
# are connected as a pipeline. All the pre-processing, database buildup,
# analysis report and graphs will be done automatically.

import os

# load the demo data, clean up and generate data report
os.system('python DataCleaning.py')
os.system('python CorrelationVis.py')
os.system('python DataInsertion_Property.py')
os.system('python DataInsertion_Label.py')
os.system('python ExportResult.py')
os.system('python XGB.py')
