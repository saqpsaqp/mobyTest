"""
	Dataset to SQLite3
	------------------
	Instructions:
	- After ./manage migrate
	- execute: python dataset2SQLite.py
"""

csv_file = '/home/squintero/mobyTest/server/nycCoD.csv'
django_home = '/home/squintero/mobyTest/server'

import django
import sys,os
sys.path.append(django_home)
os.environ['DJANGO_SETTINGS_MODULE']='server.settings'
django.setup()

import csv
from datanyc.models import Cause

dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')

for row in dataReader:
	cause = Cause()
	cause.year = row[0]
	cause.ethnicity = row[1]
	cause.sex = row[2]
	cause.cause = row[3]
	cause.count = row[4]
	cause.percent = row[5]
	cause.save()

