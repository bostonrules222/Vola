import pandas as pandas
import quandl
import csv

quandl.ApiConfig.api_key = '-Kiku-Vx2R6nNT7svt4D'
spy_ivp60 = quandl.get('VOL/SPY', column_index='30')
t = spy_ivp60.index

dates_spy = []

i = 0
for row in t:
	 dates_spy.append(str(t[i])[:10])
	 i = i + 1

with open("spy_dates.csv","w") as f:
	wr = csv.writer(f,delimiter="\n")
	wr.writerow(dates_spy)
