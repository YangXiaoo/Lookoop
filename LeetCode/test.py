# coding:utf-8

def test_numsEmpty():
	nums = []
	if nums:
		print("pass")
	else:
		print("fail")

def test_strOps():
	str1 = 'a'
	str2 = 'c'
	print(str2 - str1)

try:
	for n in gsearch1.cv_results_['mean_test_socre']:
		print("[INFO] details of gsearch1.cv_results_:{}".format(n))
except Exception as e:
	print("[ERROR] error info:{}".format(str(e)))

print("[INFO] best parameters:{}".format(gsearch1.best_params_))
print("[INFO] best scores:{}".format(gsearch1.best_score_))