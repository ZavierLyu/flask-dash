import datetime
import pandas_datareader.data as web

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime.now()
df = web.get_data_yahoo('AMZN', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True, drop=True)

print(df.head())