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

top_dct = {}
# Calcs sentiment
for stock in stock_list:
	try:
		single_quote = str("""'""")
		news_table = quandl.get_table('IFT/NSA', date=single_quote + ''.join(str(x + ',') for x in twentyone_dates),ticker=stock)
		sentiment_table = news_table[['sentiment']].to_numpy()
		news_volume = news_table[['news_volume']].to_numpy()
		if np.sum(news_volume) < 22:
			pass
		else:
			sentiment = np.sum((sentiment_table * news_volume))/np.sum(news_volume)
			top_dct[stock] = [np.sum(news_volume),round(float(sentiment),2)]
	except:
		pass
#Sorts top 30
top_dctt = sorted(top_dct.items(), key=lambda x: x[1], reverse=True)

#Sends email
sender_email = "maxarilltestdev@gmail.com"
receiver_email = "maxarilltestdev@gmail.com"
message = ''.join(str(e) for e in top_dctt)
port = 465  # For SSL
password = '123GoSox!'
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login("maxarilltestdev@gmail.com", password)
	server.sendmail(sender_email, receiver_email, message)

duration = 250  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)


