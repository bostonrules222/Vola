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
stock = str(input('Enter ticker symbol '))
days = int(input('Enter days (10,30,60,90) '))

if days == 10:
	col = '19'
	title = 'IvMean10'
	freq = 25.2
elif days == 30:
	col = '27'
	title = 'IvMean30'
	freq = 12
elif days == 60:
	col = '31'
	title = 'IvMean60'
	freq = 12
elif days == 90:
	col = '35'
	title = 'IvMean90'
	freq = 12


stock_iv = quandl.get('VOL/' + stock.upper(), column_index=col)
price_series = quandl.get('EOD/' + stock.upper(), column_index='4',)
close = price_series[['Close']].to_numpy()
iv = stock_iv[[title]].to_numpy()


inx = stock_iv.index
dates_lst = []
i = 0
for row in inx:
	dates_lst.append(str(inx[i])[:10])
	i = i + 1
rows = len(dates_lst)


inx = price_series.index
dates_lst = []
i = 0
for row in inx:
	dates_lst.append(str(inx[i])[:10])
	i = i + 1
close_len = len(dates_lst)


strads_payoff = []
strads_open_price =[]
strads_iv = []
strads_prof_perc = []
i = 0
for day in iv[0:-days]:
	open_price = close[close_len - rows + i][0]
	close_price = close[close_len - rows + i + days][0]
	the_iv = iv[i][0]
	root = math.sqrt(freq)
	std = the_iv/root
	strad = round(0.85*std*open_price,2)
	price_diff = round(abs(open_price - close_price),2)
	pl = round(strad - price_diff,2)
	strads_payoff.append(pl)
	strads_prof_perc.append(round(pl/strad,2))
	i = i + 1

#with open("payoffs.csv","w") as k:
 #   wr = csv.writer(k,delimiter="\n")
  #  wr.writerow(strads_prof_perc)
print(str(round(sum(strads_prof_perc*100)/rows,2)) + '%')