
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


train = pd.read_csv(r'C:\Study\github\Lookoops\MachineLearning\kaggle\house_prices\data\train.csv')
test = pd.read_csv(r'C:\Study\github\Lookoops\MachineLearning\kaggle\house_prices\data\test.csv')


# In[3]:


train.head()


# In[4]:


train.shape


# In[5]:


train.dtypes


# In[6]:


train['SalePrice'].describe()


# In[7]:


# 目标变量分布
sns.distplot(train['SalePrice'])


# In[8]:


# 皮尔逊相关性
# 可以查看到异常值
sns.jointplot(x='GrLivArea',y='SalePrice',data=train)


# In[9]:


# 箱线图
sns.boxplot(x="MSZoning", y="SalePrice", data=train)


# In[10]:


# 修建年代
sns.boxplot(x='YearBuilt', y='SalePrice', data=train)


# In[11]:


# 同一个属性不同值对于目标值的影响
grouped = train.groupby('OverallQual')
g1 = grouped['SalePrice'].mean().reset_index('OverallQual')
sns.barplot(x='OverallQual',y='SalePrice',data=g1)


# In[12]:


corrmatrix = train.corr()
# 绘制热力图，热力图横纵坐标分别是data的index/column,vmax/vmin设置热力图颜色标识上下限，center显示颜色标识中心位置，cmap颜色标识颜色设置
sns.heatmap(corrmatrix,square=True,vmax=1,vmin=-1,center=0.0,cmap='coolwarm')


# In[13]:


k=10
# data.nlargest(k, 'target')在data中取‘target'列值排前十的行
# cols为排前十的行的index,在本例中即为与’SalePrice‘相关性最大的前十个特征名
cols = corrmatrix.nlargest(k,'SalePrice')['SalePrice'].index
print(cols) # 打印

cm1 = train[cols].corr()
sns.heatmap(cm1,square=True,annot=True,cmap='RdPu',fmt='.2f',annot_kws={'size':10})


# In[14]:


# 通过热力图选出与目标变量相关性最强的特征
cols_k = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars','TotalBsmtSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt']
sns.pairplot(train[cols_k], size=2.5)


# In[15]:


plt.figure(figsize=(12,6))
plt.scatter(x=train.GrLivArea, y=train.SalePrice)
plt.xlabel("GrLivArea", fontsize=13)
plt.ylabel("SalePrice", fontsize=13)
plt.ylim(0,800000)
plt.show()


# In[16]:


# 查看训练数据的缺失值
null_value = train.isnull().sum()
sort_null = null_value[null_value > 0].sort_values(ascending=False)
print(sort_null)


# In[17]:


# 测试集的缺失值
test_null = test.isnull().sum()
sort_test_null = test_null[test_null > 0].sort_values(ascending=False)
print(sort_test_null)


# In[18]:


miss_none = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'GarageYrBlt', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 
            'BsmtFinType2', 'BsmtExposure', 'BsmtFinType1', 'BsmtCond', 'BsmtQual', 'MasVnrType']
miss_zero = ['MasVnrArea', 'BsmtFullBath', 'BsmtHalfBath', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'GarageCars', 'GarageArea', 'TotalBsmtSF']
miss_mode = ['Electrical', 'MSZoning', 'Utilities', 'Exterior2nd', 'Exterior1st', 'SaleType', 'Functional', 'KitchenQual']
miss_special = 'LotFrontage' # 该值为数值类型，不能用0或中值来替代,需要用与其相关性大的数据进行拟合，并且为了减少误差将该值进行分段划分


# In[19]:


# 将数据结合在一起进行处理，原则上不能这样做，训练数据与测试数据要分离
train.drop(train[(train["GrLivArea"]>4000)&(train["SalePrice"]<300000)].index,inplace=True)
full = pd.concat([train,test], ignore_index=True)
full.drop(['Id'], axis=1, inplace=True)
# full.drop(['SalePrice'], axis=1, inplace=True)


# In[20]:


for c in miss_none:
    full[c].fillna("None", inplace=True)

for c in miss_zero:
    full[c].fillna(0, inplace=True)
    
for c in miss_mode:
    full[c].fillna(full[c].mode()[0], inplace=True)


# In[21]:


full.groupby(['Neighborhood'])[['LotFrontage']].agg(['mean','median','count']) # 由Neighborhood分组并计算LotFrontage被分组后在被分组中的平均值中值及数量


# In[22]:


full.groupby(['Neighborhood', 'Street'])[['LotFrontage']].agg(['mean','median','count'])


# In[23]:


full['LotFrontage'] = full.groupby(['Neighborhood', 'Street'])[['LotFrontage']].transform(lambda x:x.fillna(x.median()))


# In[24]:


# 查看是存在缺失值
full_null = full.isnull().sum()
full_null[full_null > 0].sort_values(ascending=False)


# In[25]:


# 离散数据转换
# 将数值型大小与目标变量无关的数据进行转换
int_to_str = ['MSSubClass', 'YearBuilt', 'YearRemodAdd', 'GarageYrBlt', 'MoSold', 'YrSold' ]
for c in int_to_str:
    full[c] = full[c].astype(str)


# In[26]:


full.groupby(['MSSubClass'])[['SalePrice']].agg(['mean', 'median'])


# In[27]:


grouped = train.groupby('SaleCondition')
g1 = grouped['SalePrice'].mean().reset_index('SaleCondition')
sns.barplot(x='SaleCondition',y='SalePrice',data=g1)


# In[28]:


grouped = train.groupby('SaleType')
g1 = grouped['SalePrice'].mean().reset_index('SaleType')
sns.barplot(x='SaleType',y='SalePrice',data=g1)


# In[29]:


grouped = train.groupby('ExterQual')
g1 = grouped['SalePrice'].mean().reset_index('ExterQual')
sns.barplot(x='ExterQual',y='SalePrice',data=g1)


# In[30]:


# 评分的变量进行转换
def object_map():
    full['_MSSubClass'] = full.MSSubClass.map({
        '30' : 1, '180' : 1, '45' : 1,
         '160' : 2, '190' : 2, '90' : 2,
        '50' : 3, '85' : 3,
        '40' : 4,  '150' : 4,
        '70' : 5, '80' : 5,
        '20' : 6, '75' : 6,  '120' : 6,
        '60' : 7,
    })
    
    full['_Utilities'] = full.Utilities.map({
        'ELO' : 1,
        'NoSeWa' : 2,
        'NoSewr' : 3,
        'AllPub' : 4,
    })
    
    full['_ExterQual'] = full.ExterQual.map({
       'Ex' : 5,
       'Gd' : 4, 
       'TA' : 3, 
       'Fa' : 2, 
       'Po' : 1, 
    })
    
    full['_ExterCond'] = full.ExterCond.map({
       'Ex' : 5,
       'Gd' : 4, 
       'TA' : 3, 
       'Fa' : 2, 
       'Po' : 1, 
    })
    
    full['_BsmtQual'] = full.BsmtQual.map({
       'Ex' : 6,
       'Gd' : 5, 
       'TA' : 4, 
       'Fa' : 3, 
       'Po' : 2, 
       'None' : 1,
    })
    
    full['_BsmtExposure'] = full.BsmtExposure.map({
       'Gd' : 5,
       'Av' : 4, 
       'Mn' : 3, 
       'No' : 2, 
       'None' : 1, 
    })
    
    full['_BsmtFinType1'] = full.BsmtFinType1.map({
       'GLQ' : 7,
       'ALQ' : 6, 
       'BLQ' : 5, 
       'Rec' : 4, 
       'LwQ' : 3, 
       'Unf' : 2, 
       'None' : 1, 
    })
    
    full['_BsmtFinType2'] = full.BsmtFinType2.map({
       'GLQ' : 7,
       'ALQ' : 6, 
       'BLQ' : 5, 
       'Rec' : 4, 
       'LwQ' : 3, 
       'Unf' : 2, 
       'None' : 1, 
    })
    
    full['_HeatingQC'] = full.HeatingQC.map({
       'Ex' : 5,
       'Gd' : 4, 
       'TA' : 3, 
       'Fa' : 2, 
       'Po' : 1, 
    })
    
    full['_KitchenQual'] = full.KitchenQual.map({
       'Ex' : 5,
       'Gd' : 4, 
       'TA' : 3, 
       'Fa' : 2, 
       'Po' : 1, 
    })
    
    full['_Functional'] = full.Functional.map({
       'Typ' : 8,
       'Min1' : 7, 
       'Min2' : 6, 
       'Mod' : 5, 
       'Maj1' : 4, 
       'Maj2' : 3, 
       'Sev' : 2, 
       'Sal' : 1, 
    })
    
    full['_FireplaceQu'] = full.FireplaceQu.map({
       'Ex' : 6,
       'Gd' : 5, 
       'TA' : 4, 
       'Fa' : 3, 
       'Po' : 2, 
       'None' : 1,
    })
    
    full['_GarageType'] = full.GarageType.map({
       '2Types' : 7,
       'Attchd' : 6, 
       'Basment' : 5, 
       'BuiltIn' : 4, 
       'CarPort' : 3, 
       'Detchd' : 2, 
       'None' : 1, 
    })
    
    full['_GarageFinish'] = full.GarageFinish.map({
       'Fin' : 4,
       'RFn' : 3, 
       'Unf' : 2, 
       'None' : 1, 
    })
    
    full['_GarageQual'] = full.GarageQual.map({
       'Ex' : 6,
       'Gd' : 5, 
       'TA' : 4, 
       'Fa' : 3, 
       'Po' : 2, 
       'None' : 1,
    })
    
    full['_GarageCond'] = full.GarageCond.map({
       'Ex' : 6,
       'Gd' : 5, 
       'TA' : 4, 
       'Fa' : 3, 
       'Po' : 2, 
       'None' : 1,
    })
    
    full['_PavedDrive'] = full.PavedDrive.map({
       'Y' : 3,
       'P' : 2, 
       'N' : 1, 
    })
    
    full['_PoolQC'] = full.PoolQC.map({
       'Ex' : 5,
       'Gd' : 4, 
       'TA' : 3, 
       'Fa' : 2, 
       'None' : 1, 
    })
    
    return None


# In[31]:


object_map()


# In[32]:


full.head()


# In[33]:


k=48
corrmatrix = full.corr()
corrmatrix.nlargest(k,'SalePrice')['SalePrice'].index


# In[34]:


full.drop(['SalePrice'],axis=1,inplace=True)


# In[35]:


# test
ret = full.select_dtypes(exclude=['object'])
ret.head()


# In[36]:


from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler, StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline, make_pipeline
from scipy.stats import skew
from sklearn.decomposition import PCA, KernelPCA
from sklearn.preprocessing import Imputer 

import numpy as np


# In[37]:


class skew_dummies(BaseEstimator, TransformerMixin):
    def __init__(self, skew=0.5):
        self.skew = skew
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_numeric = X.select_dtypes(exclude=['object']) # 找到数值型数据
        skewness = X_numeric.apply(lambda x:skew(x)) # 计算偏度
        skewness_feature = skewness[abs(skewness) >= self.skew].index
        X[skewness_feature] = np.log1p(X[skewness_feature])
        X = pd.get_dummies(X) # 离散值有大小意义时进行map映射，无大小意义时进行one-hot编码
        
        return X
    
class label_encode(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        tool = LabelEncoder()
        X["YearBuilt"] = tool.fit_transform(X["YearBuilt"])
        X["YearRemodAdd"] = tool.fit_transform(X["YearRemodAdd"])
        X["GarageYrBlt"] = tool.fit_transform(X["GarageYrBlt"])
        return X
        


# In[38]:


class add_feature(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # X['add_house_sale_status'] = X['SaleCondition'] + X['SaleType'] + X['YrSold']
        X['add_house_outside_score'] = X['_PoolQC'] + X['_GarageCond'] + X['_GarageQual']
        X['add_house_inside_score'] = X['_FireplaceQu'] + X['_KitchenQual'] + X['_BsmtFinType2'] + X['_BsmtFinType1'] + X['_BsmtQual']
        X['add_house_based_score'] = X['_HeatingQC'] + X['_Utilities']
        X['add_house_wall_roof_score'] = X['_ExterCond'] + X['_ExterQual']
        
        X["Bsmt"] = X["BsmtFinSF1"] + X["BsmtFinSF2"] + X["BsmtUnfSF"]
        X["Rooms"] = X["FullBath"]+X["TotRmsAbvGrd"]
        X["PorchArea"] = X["OpenPorchSF"]+X["EnclosedPorch"]+X["3SsnPorch"]+X["ScreenPorch"]
        X["TotalPlace"] = X["TotalBsmtSF"] + X["1stFlrSF"] + X["2ndFlrSF"] + X["GarageArea"] + X["OpenPorchSF"]+ X["EnclosedPorch"]+ X["3SsnPorch"]+ X["ScreenPorch"]
        return X


# In[39]:


full.shape


# In[40]:


pipe = Pipeline([
    ('label_encode', label_encode()),
    ('skew_dummies', skew_dummies(skew=1)),
    ('add_feature', add_feature()),
])


# In[41]:


full_pipe = pipe.fit_transform(full)


# In[42]:


full_pipe.shape


# In[43]:


full_null = full_pipe.isnull().sum()
full_null[full_null > 0].sort_values(ascending=False)


# In[44]:


scaler = RobustScaler()


# In[45]:


train_index = train.shape[0]
train_x = full_pipe[:train_index]
test_x = full_pipe[train_index:]
train_y = train.SalePrice


# In[46]:


train_x_scaled = scaler.fit(train_x).transform(train_x)
train_y_scaled = np.log(train_y)
test_x_scaled = scaler.transform(test_x)


# In[47]:


pca = PCA(n_components=350) # 保留350个特征


# In[48]:


train_x_pca = pca.fit_transform(train_x_scaled)
test_x_pca = pca.transform(test_x_scaled)


# In[49]:


train_x_pca.shape, test_x_pca.shape


# In[50]:


from sklearn.model_selection import cross_val_score, GridSearchCV, KFold
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, AdaBoostRegressor, BaggingRegressor
from sklearn.svm import SVR, LinearSVR
from sklearn.linear_model import ElasticNet, SGDRegressor, BayesianRidge
from sklearn.kernel_ridge import KernelRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor


# In[51]:


def cv_rmse(model, X, y):
    # cross_val_score函数用法：https://www.cnblogs.com/lzhc/p/9175707.html
    rmse = np.sqrt(-cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=5))
    return rmse


# In[52]:


models = [LinearRegression(),
          Ridge(), # http://www.cnblogs.com/pinard/p/6023000.html
          Lasso(alpha=0.01,max_iter=10000), # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html
          RandomForestRegressor(), # https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.RandomForestRegressor.html
          GradientBoostingRegressor(), # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html
          SVR(), # https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR
          LinearSVR(), # https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html
          ElasticNet(alpha=0.001,max_iter=10000), # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html
          SGDRegressor(max_iter=10000,tol=1e-3), # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html
          BayesianRidge(), # 
          KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5), # https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html
         ExtraTreesRegressor(), # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html
          XGBRegressor(), 
          AdaBoostRegressor(n_estimators=50), # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html
          BaggingRegressor(), # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html
          DecisionTreeRegressor(), #https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
          KNeighborsRegressor()] # https://scikit-learn.org/0.18/modules/generated/sklearn.neighbors.KNeighborsRegressor.html


# In[53]:


names = ["LR", "Ridge", "Lasso", "RF", "GBR", "SVR", "LinSVR", "Ela","SGD","Bay","Ker","Extra","Xgb", "AdaBoost", "Bagging", "DT", "KN"]
for name, model in zip(names, models):
    score = cv_rmse(model, train_x_pca, train_y_scaled)
    print("{}: {:.6f}, {:.4f}".format(name,score.mean(),score.std()))


# In[54]:


class grid():
    def __init__(self, model):
        self.model = model
        
    def grid_train(self, X, y, train_para):
        grid_search = GridSearchCV(self.model, train_para, cv=5, scoring="neg_mean_squared_error")
        grid_search.fit(X, y)
        print(grid_search.best_params_, np.sqrt(-grid_search.best_score_)) # 打印最好的结果
        grid_search.cv_results_['mean_test_score'] = np.sqrt(-grid_search.cv_results_['mean_test_score'])
        print(pd.DataFrame(grid_search.cv_results_)[['params','mean_test_score','std_test_score']])


# In[55]:


grid(Lasso()).grid_train(train_x_pca,train_y_scaled,{'alpha': [0.002, 0.0003, 0.00035, 0.0004,0.0005,0.0007,0.0006,0.0009,0.0008], 'max_iter':[10000]})


# In[56]:


# 获得最佳参数的另一种写法
ridgecv = RidgeCV(alphas=[0.01, 0.1, 0.5, 1, 3, 5, 7, 8, 9, 10, 11, 15, 18, 20, 100]) 
ridgecv.fit(train_x_pca, train_y_scaled)
ridgecv.alpha_  


# In[57]:


grid(Ridge()).grid_train(train_x_pca,train_y_scaled,{'alpha':[i for i in range(10, 20)]})


# In[58]:


grid(GradientBoostingRegressor()).grid_train(train_x_pca,train_y_scaled,{'learning_rate':[float(i/10) for i in range(1, 10)]})


# In[59]:


grid(SVR()).grid_train(train_x_pca,train_y_scaled,
                       {
                           'kernel':['rbf'], 
                           'gamma':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5],
                           'epsilon':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5, 1, 10]
                       })


# In[60]:


grid(LinearSVR()).grid_train(train_x_pca,train_y_scaled,{'epsilon':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5], 'loss':['epsilon_insensitive', 'squared_epsilon_insensitive']})


# In[61]:


grid(GradientBoostingRegressor()).grid_train(train_x_pca,train_y_scaled,{'learning_rate':[float(i/10) for i in range(1, 10)]})


# In[63]:


grid(LinearSVR()).grid_train(train_x_pca,train_y_scaled,{'epsilon':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5], 'loss':['epsilon_insensitive', 'squared_epsilon_insensitive']})


# In[64]:


grid(ElasticNet()).grid_train(train_x_pca,train_y_scaled,{'alpha':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5],'l1_ratio':[0.08,0.1,0.3,0.5,0.7],'max_iter':[10000]})


# In[70]:


grid(SGDRegressor()).grid_train(train_x_pca,train_y_scaled,{'alpha':[0.005, 0.01, 0.05, 0.1,0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 5],'l1_ratio':[0.08,0.1,0.3,0.5,0.7, 0.8, 0.9, 1]})


# In[100]:


grid(KernelRidge()).grid_train(train_x_pca,train_y_scaled,{'alpha':[0.05, 0.1, 0.3,0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 5], 'kernel':['polynomial'], 'coef0':[1, 1.2, 1.5, 1.6, 1.8, 1.9, 2, 2.2, 2.5, 3]})


# In[111]:


# 集成学习
class stacking(BaseEstimator, RegressorMixin, TransformerMixin):
    def __init__(self, model, fusion_model):
        self.model = model
        self.fusion_model = fusion_model
        self.kf = KFold(n_splits=14, random_state=50, shuffle=True)
        
    def fit(self, X, y):
        self.model_saved = [list() for i in self.model] 
        train_pred = np.zeros((X.shape[0], len(self.model))) # 存储每个数据被预测的结果， 其结果使用融合模型进行训练
        
        for i,mod in enumerate(self.model):
            for train_index, value_index in self.kf.split(X, y):
                tmp_model = clone(mod)
                tmp_model.fit(X[train_index], y[train_index])
                self.model_saved[i].append(tmp_model)
                train_pred[value_index, i] = tmp_model.predict(X[value_index])
        self.fusion_model.fit(train_pred, y) # 将训练数据预测结果作为融合模型的输入训练数据
        
        return self
    
    def predict(self, X):
        test_mean = np.column_stack([np.column_stack(mod.predict(X) for mod in tmp_model).mean(axis=1) for tmp_model in self.model_saved]) # 对每个test数据进行预测并取平局值
        return self.fusion_model.predict(test_mean)


# In[112]:


train_model = [Ridge(alpha=17),
          Lasso(alpha=0.0003,max_iter=10000),
          RandomForestRegressor(),
          GradientBoostingRegressor(learning_rate=0.2),
          SVR(epsilon=0.01, gamma=0.005, kernel="rbf"), 
          LinearSVR(epsilon=0.001, loss="epsilon_insensitive"), 
          ElasticNet(alpha=0.0005, l1_ratio=0.5, max_iter=10000), 
          SGDRegressor(alpha=0.3, l1_ratio=0.3),
          BayesianRidge(), 
          KernelRidge(alpha=0.3, kernel='polynomial', degree=2, coef0=1.5),
          XGBRegressor(), 
          AdaBoostRegressor(n_estimators=50),
          BaggingRegressor(),
          KNeighborsRegressor()]


# In[113]:


stack_model = stacking(train_model, KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5))


# In[114]:


X = Imputer().fit_transform(train_x_pca)
y = Imputer().fit_transform(train_y_scaled.values.reshape(-1,1)).ravel()


# In[115]:


stack_model.fit(X, y)


# In[116]:


pred = np.exp(stack_model.predict(test_x_pca))


# In[117]:


result = pd.DataFrame({'Id':test.Id, 'SalePrice':pred})
result.to_csv("submission.csv",index=False)


# In[118]:


test_stack_model = stacking(train_model, KernelRidge(alpha=0.3, kernel='polynomial', degree=2, coef0=1.5))


# In[119]:


print(cv_rmse(test_stack_model,X,y))


# In[120]:


print(cv_rmse(test_stack_model,X,y).mean())

