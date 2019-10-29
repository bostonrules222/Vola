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

#Gets stock list
stock_list = []
with open('stock_list.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		for row in row:
			stock_list.append(row)
			
# Calculates IV change from yesterday to today (by %), places in a dct

iv_dct = {}
for stock in stock_list:
	try:
		pull = quandl.get('VOL/' + stock, column_index='27', start_date=yesterday, end_date=today)
		Iv30 = pull[['IvMean30']].to_numpy()
		diff = (Iv30[1][0] - Iv30[1][0])/ Iv30[0][0]
		iv_dct[stock] = round(float(diff*100),2)
	except:
		pass

max_vall = sorted(iv_dct.items(), key=lambda x: x[1], reverse=True)


# Sends email

sender_email = "maxarilltestdev@gmail.com"
receiver_email = "maxarilltestdev@gmail.com"
message = ''.join(str(e) for e in max_vall)
port = 465  # For SSL
password = '123GoSox!'
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login("maxarilltestdev@gmail.com", password)
	server.sendmail(sender_email, receiver_email, message)

duration = 500  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
