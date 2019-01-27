# coding:utf-8
# 2019-1-20
# house prices

# https://blog.csdn.net/huangxiaoyun1900/article/details/82229708
# 编码： http://www.cnblogs.com/king-lps/p/7846414.html
# 博客园：https://www.cnblogs.com/massquantity/p/8640991.html


import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
# sns.set(style="white", color_codes=True)


train = pd.read_csv(r'C:\Study\github\Lookoops\MachineLearning\kaggle\house_prices\data\train.csv')
test = pd.read_csv(r'C:\Study\github\Lookoops\MachineLearning\kaggle\house_prices\data\test.csv')


head_five = train.head()
print(head_five)
# """
#    Id  MSSubClass MSZoning    ...     SaleType  SaleCondition SalePrice
# 0   1          60       RL    ...           WD         Normal    208500
# 1   2          20       RL    ...           WD         Normal    181500
# 2   3          60       RL    ...           WD         Normal    223500
# 3   4          70       RL    ...           WD        Abnorml    140000
# 4   5          60       RL    ...           WD         Normal    250000

# [5 rows x 81 columns]
# """

# 数据分布
train_shape = train.shape
print(train_shape)
# # (1460, 81)


# 特征类型
train_dtypes = train.dtypes
print(train_dtypes)
"""
Id                 int64
MSSubClass         int64
MSZoning          object
LotFrontage      float64
LotArea            int64
                  ...   
SaleCondition     object
SalePrice          int64
Length: 81, dtype: object
"""


# 分析目标变量
sale_price = train['SalePrice'].describe()
print("分析目标变量")
print(sale_price)
"""
count      1460.000000
mean     180921.195890
std       79442.502883
min       34900.000000
25%      129975.000000
50%      163000.000000
75%      214000.000000
max      755000.000000
Name: SalePrice, dtype: float64
"""


############################## 可视化 ###################################
# 目标变量分布
# http://seaborn.pydata.org/generated/seaborn.distplot.html
distplot = sns.distplot(train['SalePrice'])
plt.savefig('SalePrice')
plt.show()

# 查看房价关于其中一个参数的分布

# 皮尔逊相关性
sns.jointplot(x='GrLivArea',y='SalePrice',data=train)
plt.savefig('GrLivArea_SalePrice')
plt.show()

# 箱型图
sns.boxplot(x="MSZoning", y="SalePrice", data=train)
plt.savefig('MSZoning_SalePrice')
plt.show()


# 修建年代
sns.boxplot(x='YearBuilt', y='SalePrice', data=train)
plt.savefig('YearBuilt_SalePrice')
plt.show()


# 柱状图
# 使用groupby将价格按照特征分类，再去平均值，使用柱状图展示

# 由柱状图可以看出随着overall评分越高, 房屋平均价格越高
grouped = train.groupby('OverallQual')
g1 = grouped['SalePrice'].mean().reset_index('OverallQual')
sns.barplot(x='OverallQual',y='SalePrice',data=g1)
plt.savefig('OverallQual_SalePrice')
plt.show()


# 热力图
# 计算相关系数
corrmatrix = train.corr()
# 绘制热力图，热力图横纵坐标分别是data的index/column,vmax/vmin设置热力图颜色标识上下限，center显示颜色标识中心位置，cmap颜色标识颜色设置
sns.heatmap(corrmatrix,square=True,vmax=1,vmin=-1,center=0.0,cmap='coolwarm')
plt.savefig('heatmap')
plt.show()

# 取相关性前10的特征
k=10
# data.nlargest(k, 'target')在data中取‘target'列值排前十的行
# cols为排前十的行的index,在本例中即为与’SalePrice‘相关性最大的前十个特征名
cols = corrmatrix.nlargest(k,'SalePrice')['SalePrice'].index

cm = np.corrcoef(train[cols].values.T)
# data[cols].values.T
# 设置坐标轴字体大小
sns.set(font_scale=1.25)
# sns.heatmap() cbar是否显示颜色条，默认是；cmap显示颜色；annot是否显示每个值，默认不显示；
# square是否正方形方框，默认为False,fmt当显示annotate时annot的格式；annot_kws为annot设置格式
# yticklabels为Y轴刻度标签值，xticklabels为X轴刻度标签值
hm = sns.heatmap(cm,cmap='RdPu',annot=True,square=True,fmt='.2f',annot_kws={'size':10},yticklabels=cols.values,xticklabels=cols.values)
 
 
# 上例提供了求相关系数另一种方法，也可以直接用data.corr(),更方便
cm1 = train[cols].corr()
hm2 = sns.heatmap(cm1,square=True,annot=True,cmap='RdPu',fmt='.2f',annot_kws={'size':10})
plt.savefig('heatmap_10')
plt.show()


# 通过热力图选出与目标变量相关性最强的特征
cols_k = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars','TotalBsmtSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt']
sns.pairplot(train[cols_k], size=2.5)
plt.savefig('pairplot_10')
plt.show()



# 查看前10个与目标值相关性最高的属性并通过这些属性查看异常值
k=10
corrmatrix = train.corr()
cols = corrmatrix.nlargest(k,'SalePrice')['SalePrice'].index
print(cols)
# Index(['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea',
#        'TotalBsmtSF', '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt'],
#       dtype='object')


# 查看异常值
plt.figure(figsize=(12,6))
plt.scatter(x=train.GrLivArea, y=train.SalePrice)
plt.xlabel("GrLivArea", fontsize=13)
plt.ylabel("SalePrice", fontsize=13)
plt.ylim(0,800000)
plt.show()

# ....省略剩下的属性




############################## 数据清洗 ###################################

# 查看缺失值
null_value = train.isnull().sum()
sort_null = null_value[null_value > 0].sort_values(ascending=False)
print(sort_null)
# """
# PoolQC          1453 # pool quality, object, score
# MiscFeature     1406 # Miscellaneous feature not covered in other categories, object
# Alley           1369 # Type of alley access to property, object
# Fence           1179 # Fence quality, object, score, no fence
# FireplaceQu      690 # Fireplace quality, object, score, No Fireplace
# LotFrontage      259 # Linear feet of street connected to property, int
# GarageYrBlt       81 # Year garage was built, int
# GarageType        81 # Garage location, object
# GarageFinish      81 # Interior finish of the garage, object
# GarageQual        81 # Garage quality, object, score, No Garage
# GarageCond        81 # Garage condition, object, score
# BsmtFinType2      38 # Rating of basement finished area (if multiple types), object, score, No Garage
# BsmtExposure      38 # Refers to walkout or garden level walls, object
# BsmtFinType1      37 # Rating of basement finished area, object, score, No Basement
# BsmtCond          37 # Evaluates the general condition of the basement, object, score
# BsmtQual          37 # Evaluates the height of the basement, object, score
# MasVnrArea         8 # Masonry veneer area in square feet(砖石贴面面积(平方英尺)), int
# MasVnrType         8 # Masonry veneer type, object
# Electrical         1 # Electrical system, object
# """

test_null = test.isnull().sum()
sort_test_null = test_null[test_null > 0].sort_values(ascending=False)
print("测试集缺失值")
print(sort_test_null)
"""
PoolQC          1456
MiscFeature     1408
Alley           1352
Fence           1169
FireplaceQu      730 # Fireplace quality, object, socre
LotFrontage      227
GarageYrBlt       78
GarageCond        78
GarageQual        78
GarageFinish      78
GarageType        76
BsmtCond          45
BsmtExposure      44
BsmtQual          44
BsmtFinType1      42
BsmtFinType2      42
MasVnrType        16
MasVnrArea        15
MSZoning           4 # Identifies the general zoning classification of the sale. object, half score, model
BsmtFullBath       2 # Basement full bathrooms, int, default 0
BsmtHalfBath       2 # Basement half bathrooms, int, default 0
Utilities          2 # Type of utilities available, object, score, lost
Functional         2 # Home functionality (Assume typical unless deductions are warranted), object, score
Exterior2nd        1 # Exterior covering on house (if more than one material), object
Exterior1st        1 # Exterior covering on house, object, half score
SaleType           1 # Type of sale, object, half score
BsmtFinSF1         1 # Type 1 finished square feet, int, default 0
BsmtFinSF2         1 # Type 2 finished square feet, int, default 0
BsmtUnfSF          1 # Unfinished square feet of basement area, int, default 0
KitchenQual        1 # Kitchen quality, object, socre， None取中位数
GarageCars         1 # Size of garage in car capacity, int
GarageArea         1 # Size of garage in square feet, int
TotalBsmtSF        1 # Total square feet of basement area, int
"""

# # 补全缺失值
# ret =  train[(train["GrLivArea"]>4000)&(train["SalePrice"]<300000)].index
# print(ret)


