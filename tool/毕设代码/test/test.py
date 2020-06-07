from datetime import datetime 
startDay = datetime(2020, 3, 8)
today = datetime.today()
print(today)
info = (today - startDay).days
print(info)