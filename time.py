import datetime
import time


datetime.datetime.now()
datetime.datetime(2020, 1, 6, 15, 8, 24, 78915)

res = f'{datetime.datetime.now()}'
while True:
	s = f'{datetime.datetime.now()}'
	print(s[:-7])
	time.sleep(1)
