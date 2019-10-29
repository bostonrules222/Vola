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
stock1 = str(input('Enter ticker symbol 1 '))
stock2 = str(input('Enter ticker symbol 2 '))

get_1 = quandl.get('EOD/' + stock1.upper(), column_index='4')
get_2 = quandl.get('EOD/' + stock2.upper(), column_index='4')
inx = get_1.index
dates_lst = []
i = 0
for row in inx:
	dates_lst.append(str(inx[i])[:10])
	i = i + 1
s1l = len(dates_lst)
inx = get_2.index
dates_lst = []
i = 0
for row in inx:
	dates_lst.append(str(inx[i])[:10])
	i = i + 1
s2l = len(dates_lst)
rows = min(s1l,s2l)


prices_1_np = get_1[['Close']].to_numpy()
i = s1l - rows
prices_1 = []
for array in prices_1_np[s1l - rows:]:
	prices_1.append(prices_1_np[i][0])
	i = i + 1

prices_2_np = get_2[['Close']].to_numpy()
i = s2l - rows
prices_2 = []
for array in prices_2_np[s2l - rows:]:
	prices_2.append(prices_2_np[i][0])
	i = i + 1 


print(np.corrcoef(np.array(prices_2),np.array(prices_1)))
