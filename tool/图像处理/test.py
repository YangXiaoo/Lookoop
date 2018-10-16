import numpy as np 
import datetime
nums = [1,2,3,4,5]
for i in range(len(nums)):
	nums[i] = str(nums[i])
print("\t".join(nums))