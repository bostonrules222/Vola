#Imports
import quandl
import numpy as np
import pandas as pd
import datetime as dt
import csv
import sys
import smtplib, ssl
import math
import winsound
quandl.ApiConfig.api_key = '-Kiku-Vx2R6nNT7svt4D'

#Gets today's and yesterday's dates
dates_get = quandl.get('VOL/SPY', column_index='1')
inx = dates_get.index
dates_lst = []
i = 0
for row in inx:
	dates_lst.append(str(inx[i])[:10])
	i = i + 1

today = str((dates_lst[-1]))
yesterday = str((dates_lst[-2]))
twentyone_dates = dates_lst[-22:-1]

#Gets stock list
stock_list = []
with open('stock_list.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		for row in row:
			stock_list.append(row)

# Calcs sentiment
single_quote = str("""'""")
for stock in stocks_list:
	single_quote = str("""'""")
	news_table = quandl.get_table('IFT/NSA', date=single_quote + ''.join(str(x + ',') for x in twentyone_dates),ticker=stock)
	sentiment_table = news_table[['sentiment']].to_numpy()
	news_volume = news_table[['news_volume']].to_numpy()
	sentiment = np.sum((sentiment_table * news_volume))/np.sum(news_volume)
	average_volume = np.average(news_volume)
	today_volume = news_volume[-1][0]
	news_buzz = today_volume/average_volume
	

