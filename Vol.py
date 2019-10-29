import quandl
import numpy as np
import pandas as pd
quandl.ApiConfig.api_key = '-Kiku-Vx2R6nNT7svt4D'
stock = str("VOL/") + str(input('Enter company symbol'))
stock_iv60 = quandl.get(stock.upper(), column_index='31')
stock_hv60 = quandl.get(stock.upper(), column_index='4')
hv60 = stock_hv60[['Hv60']].to_numpy()
iv60 = stock_iv60[['IvMean60']].to_numpy()
avgiv = np.average(iv60)
avghv = np.average(hv60)
medianiv = np.median(iv60)
medianhv = np.median(hv60)
print(avgiv)
print(avghv)
print(avgiv - avghv)
print(medianiv)
print(medianhv)
print(medianiv - medianhv)