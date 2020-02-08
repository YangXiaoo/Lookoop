# coding:utf-8
# 2020-2-7
# 样本数据分析脚本

import sys 
sys.path.append("../")

import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt

from util import io, tool
import datetime

from trainModel import logger

TODAY = str(datetime.datetime.today()).split(" ")[0]

csvDataSavingPath = "../data/samples-csv.csv"
picSavingDir = "dataAnalysisResults/{}".format(TODAY)
label = 'force'

def checkDir():
	tool.mkdirs(picSavingDir)

checkDir()

data = pd.read_csv(csvDataSavingPath)

# 目标变量分布
obj = data[label].describe()
logger.info(obj)
# count       30.000000
# mean     38658.995167
# std        589.833248
# min      37650.160000
# 25%      38150.199000
# 50%      38553.244500
# 75%      39065.474750
# max      39840.227000

distplot = sns.distplot(data[label],norm_hist=False)
plt.savefig('{}/{}.jpg'.format(picSavingDir, label))
# plt.show()


# 皮尔逊相关系数计算
corrmatrix = data.corr()	
logger.info(corrmatrix)
# 		  y1        z1        z2        x2        x3     force
# y1     1.000000 -0.376928 -0.227836 -0.054728  0.118595 -0.022985
# z1    -0.376928  1.000000 -0.092026 -0.201551 -0.418984 -0.201572
# z2    -0.227836 -0.092026  1.000000 -0.433553 -0.176537 -0.066349
# x2    -0.054728 -0.201551 -0.433553  1.000000  0.306022 -0.187176
# x3     0.118595 -0.418984 -0.176537  0.306022  1.000000 -0.015420
# force -0.022985 -0.201572 -0.066349 -0.187176 -0.015420  1.000000

# 皮尔逊相关系数的热图
sns.heatmap(corrmatrix,square=True,vmax=1,vmin=-1,center=0.0,cmap='coolwarm')
plt.savefig('{}/heatmap.jpg'.format(picSavingDir))
# plt.show()

# topk热图
k = 6
cols = corrmatrix.nlargest(k,label)[label].index
cm1 = data[cols].corr()
hm2 = sns.heatmap(cm1,square=True,annot=True,cmap='RdPu',fmt='.2f',annot_kws={'size':5})
plt.savefig('{}/heatMap_top{}.jpg'.format(picSavingDir, k))

# 单个变量与标签之间的皮尔逊相关系数
for h in data.columns.values[:-1]:
	sns.jointplot(x=h,y=label,data=data)
	plt.savefig('{}/{}_{}.jpg'.format(picSavingDir, h, label))