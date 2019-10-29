#---Imports---#
import quandl
import numpy as np
import pandas as pd
import datetime as dt
import csv
import sys
import smtplib, ssl
import math
quandl.ApiConfig.api_key = '-Kiku-Vx2R6nNT7svt4D'


# Gets today's and yesterday's dates
dates_get = quandl.get('VOL/SPY', column_index='1')
inx = dates_get.index
dates_lst = []
i = 0
for row in inx:
	 dates_lst.append(str(inx[i])[:10])
	 i = i + 1
today = str((dates_lst[-1]))
yesterday = str((dates_lst[-2]))


# Gets stock csv and turns into list, filters by volume
stocks_raw = []
stock_list = []
minvolume = 40000000 
with open('1bmc.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
    	stocks_raw.append(row[0])
for stock in stocks_raw:
	try:
		sp = quandl.get('EOD/' + stock, column_index='4', start_date=today, end_date=today)
		price = sp[['Close']].to_numpy()
		sv = quandl.get('EOD/' + stock, column_index='5', start_date=today, end_date=today)
		volume = sv[['Volume']].to_numpy()
		if price[0][0] * volume[0][0] > minvolume:
			stock_list.append(stock)
		else:
			pass
	except:
		pass
with open("stock_list.csv","w") as k:
    wr = csv.writer(k,delimiter="\n")
    wr.writerow(stock_list)
