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

news_table = quandl.get_table('IFT/NSA', date=single_quote + ''.join(str(x + ',') for x in twentyone_dates),ticker=stock)
sentiment_table = news_table[['sentiment']].to_numpy()
print(news_table)
print(sentiment)