#santa tracker
from datetime import datetime


today_date = datetime.now()

christmas_date = datetime(2022, 12, 25, 0, 0, 0)

santa_distance = christmas_date - today_date

print('There is ' + str(santa_distance.days) + ' days until santa cums!')
