import numpy as np 
import datetime
start_time = datetime.datetime.now()
for i in range(2000000):
	pass
end_time = datetime.datetime.now()
expend = end_time - start_time
print(expend*2000)