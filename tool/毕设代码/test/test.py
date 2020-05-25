from datetime import datetime, date 

startDay = datetime(2020, 3, 9)
today = datetime.today()
print((today - startDay).days)