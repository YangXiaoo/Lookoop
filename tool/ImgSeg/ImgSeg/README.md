
# 图像阈值分割【c++版本】
##### [github地址](https://github.com/YangXiaoo/Lookoop/tree/master/tool/ImgSeg/ImgSeg "github地址")
---
使用softmax对阈值进行拟合
## 主要步骤
### 1. 生成不同阈值分割的图片
使用不同阈值对图像进行二值化得到不同的图片，从中选择最佳阈值作为训练参数。
使用代码见程序`gen_diff_threshed_img.cpp`
### 2.使用softmax分类
详细代码见`MLCore.hpp`, `MLCore.cpp`。
### 3.获得待分割图像直方图进行预测
见代码`segmentation_main.cpp`。

---
# 图像阈值分割【python版本】
##### [github地址](https://github.com/YangXiaoo/Lookoop/tree/master/tool/图像处理/handle_segement "github地址")
### 1. 生成不同阈值分割的图片
见代码`select_thresh_value.py`
### 2.使用softmax分类
见代码`softmax.py`。
### 3.获得待分割图像直方图进行预测
见代码`softmaxWithNorm.py`，该程序对图像进行了裁剪并resize到指定尺寸。`softmaxWithoutNorm.py`则未裁剪。

## 注
python版本还提供了多种方法如：
- `dbscanWithNorm.py`[使用SIF特征检测获得手掌特征，并使用聚类法采集阈值]

- `histogramMeanWithNorm.py`[直方图均值]

- `maxEntropyWithNorm.py`[最大熵]

- `OtsuWithNorm.py`[大津法]

- `regressionWithNorm.py`[回归法]

还可以使用其余分类法如 gbdt, xgbdt, adaboost, RF....
