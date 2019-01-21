# coding:UTF-8
import pandas as pd
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

bone = pd.read_csv(r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset.csv')
bone.head()
print(bone.head()) # 打印前5排数据
"""
     id  boneage   male
0  1377      180  False
1  1378       12  False
2  1379       94  False
3  1380      120   True
4  1381       82  False
"""
# Press shift+enter to execute this cell
ret = bone["boneage"].value_counts()
# print(ret)
"""
156    1113
       ... 
20        1
Name: boneage, Length: 160, dtype: int64
"""
# bone.plot(kind="scatter", x="boneage", y="id")



# 男女各年龄分布图
csv_data = pd.DataFrame(bone)  
bone_x, bone_male_y_dict, bone_female_y_dict = [], {}, {}
for i in range(len(csv_data)):
    bone_age = csv_data['boneage'][i]
    is_male = csv_data['male'][i]
    # print(is_male)
    if bone_age not in bone_x:
        bone_x.append(bone_age)
    if is_male == True:
        bone_male_y_dict[bone_age] = bone_male_y_dict.get(bone_age, 0) + 1
    else:
        bone_female_y_dict[bone_age] = bone_female_y_dict.get(bone_age, 0) + 1
# print(bone_male_y_dict)
# print(bone_female_y_dict)
bone_x.sort()
bone_male_y, bone_female_y = [], []
# print(bone_x)

for i in bone_x:
    bone_male_y.append(bone_male_y_dict.get(i, 0))
    bone_female_y.append(bone_female_y_dict.get(i, 0))
# print(len(bone_x) == len(bone_male_y))
fig, (axs1, axs2) = plt.subplots(1, 2, figsize=(15,15))
axs1.scatter(bone_x, bone_male_y, color="k")
axs1.set_title('male')
axs1.set_xlabel('bone_age')
axs1.set_ylabel('total')

axs2.scatter(bone_x, bone_female_y, color="red")
axs2.set_title('female')
axs2.set_xlabel('bone_age')
axs2.set_ylabel('total')

plt.show()



# sns.jointplot(x="age", y="people", data=iris, size=5)

# 箱图
sns.boxplot(x="male", y="boneage", data=bone)
plt.show()

# 箱图+数据分布散点图
ax = sns.boxplot(x="male", y="boneage", data=bone)
ax = sns.stripplot(x="male", y="boneage", data=bone, jitter=True, edgecolor="gray")
plt.show()

# 小提琴分布图
sns.violinplot(x="male", y="boneage", data=bone, size=6)
plt.show()

# 双变量分布图
sns.pairplot(bone.drop("id", axis=1), hue="male", size=2)
plt.show()

# 箱图
bone.drop("id", axis=1).boxplot(by="male", figsize=(12, 6))
plt.show()

from pandas.tools.plotting import andrews_curves
plt.figure()
andrews_curves(bone.drop("id", axis=1), "male")
plt.show()