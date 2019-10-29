import csv
import sys
import quandl
import numpy as np
import pandas as pd
from statistics import mean 
from statistics import median
quandl.ApiConfig.api_key = '-Kiku-Vx2R6nNT7svt4D'


quandl.get('VOL/SPY', column_index='30')
spy_ivp60 = quandl.get('VOL/SPY', column_index='30')
ar = spy_ivp60[['IvPut60']].to_numpy()



ivs = []
for num in ar:
	ivs.append(float(num))

with open("put60_ivs.csv","w") as f:
	wr = csv.writer(f,delimiter="\n")
	wr.writerow(ivs)