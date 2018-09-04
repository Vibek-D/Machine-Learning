#This file get latest stock trends for a given company which is specified in the comm
#command line

import numpy as np
import pandas as pd
import datetime
from sklearn import preprocessing
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
import operator
import re
from dateutil import parser
import json
import requests
import urllib
from pandas_datareader import data
import sys



if '__name__'== 'main':
	company = sys.argv[1]
	start_date = sys.argv[2]
	end_date = sys.argv[3]
	data = data.DataReader(company, 'yahoo', start_date , end_date)
	data.to_csv('Data/'+company+'.csv')
