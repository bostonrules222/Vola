import quandl
import numpy as np
import pandas as pd
import datetime as dt
import math
quandl.ApiConfig.api_key = '-Kiku-Vx2R6nNT7svt4D'
stock = str(input('Enter ticker symbol '))

# Gets today's, yesterday's, and 21 days dates
dates_get = quandl.get('VOL/' + stock.upper(), column_index='1')
inx = dates_get.index
dates_lst = []
i = 0
for row in inx:
	dates_lst.append(str(inx[i])[:10])
	i = i + 1
today = str((dates_lst[-1]))
yesterday = str((dates_lst[-2]))
days21 = str((dates_lst[-22]))
twentyone_dates = dates_lst[-22:-1]


# Gets values
stock_iv30_21 = quandl.get('VOL/' + stock.upper(), column_index='27', start_date=days21, end_date=today)
stock_hv30_21 = quandl.get('VOL/' + stock.upper(), column_index='3', start_date=days21, end_date=today)
price_series = quandl.get('EOD/' + stock.upper(), column_index='4', start_date=yesterday, end_date=today)

#Close
close = price_series[['Close']].to_numpy()[1][0]
print("Close")
print(close)
#Change %
print('Change %')
close_yest = price_series[['Close']].to_numpy()[0][0]
print(format(100*(close - close_yest)/close_yest,'.2f') + "%")
#Change Std
print('STD Move')
Iv30 = stock_iv30_21[['IvMean30']].to_numpy()
std = (Iv30[-2][0]/math.sqrt(252)) * close_yest
std_move = print(format(abs((close - close_yest)/std),'.2f'))
#Current Iv30
print('Current 30IV')
print(format(stock_iv30_21[['IvMean30']].to_numpy()[-1][0]*100,'.2f'))
#Current Hv30
print('Current 30HV')
print(format(stock_hv30_21[['Hv30']].to_numpy()[-1][0]*100,'.2f'))
#Average 21Iv30
print('Average IV past 30 days')
mean_iv = stock_iv30_21[['IvMean30']].to_numpy()
print(format(np.average(mean_iv)*100,'.2f'))
#Average 21Hv30
print('Average HV past 30 days')
mean_hv = stock_hv30_21[['Hv30']].to_numpy()
print(format(np.average(mean_hv)*100,'.2f'))

single_quote = str("""'""")
news_table = quandl.get_table('IFT/NSA', date=single_quote + ''.join(str(x + ',') for x in twentyone_dates),ticker=stock)
news_day_table = quandl.get_table('IFT/NSA', date=today,ticker=stock)
#Sentiment
print('Sentiment')
sentiment_table = news_table[['sentiment']].to_numpy()
news_volume = news_table[['news_volume']].to_numpy()
sentiment = np.sum((sentiment_table * news_volume))/np.sum(news_volume)
print(round(float(sentiment),2))
#News Buzz
print('Buzz')
average_volume = np.average(news_volume)
today_volume = news_volume[-1][0]
news_buzz = today_volume/average_volume
print(round(float(news_buzz),2))
print('Articles past month')
print(np.sum(news_volume))
