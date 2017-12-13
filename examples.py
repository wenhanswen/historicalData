from datetime import datetime

from gdax import GDAX


def btc_usd_30min(start, end):
  return GDAX('BTC-USD').fetch(start, end, 30)


def ltc_eur_1day(start, end):
  return GDAX('LTC-EUR').fetch(start, end, 1440)


if __name__ == "__main__":
  data_frame = ltc_eur_1day(datetime(2017, 7, 1), datetime(2017, 9, 10))
  print (data_frame)

  # Save to CSV.
  data_frame.to_csv('data.csv')
