import write_data
import pandas as pd
from datetime import datetime

def get_stock_dataframe(symbol):
	filename = 'Data/'+symbol+'.csv'
	df = pd.read_csv(filename,header = 0)
	return df



if '__name__' == 'main':
	df = get_stock_dataframe('AAPL')
	print df.head()