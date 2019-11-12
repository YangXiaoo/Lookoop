## 数值实验设计
1. 确定自由变形点位置及数量
    - sculptor
2. 各变形点的取值范围
    - 完成
3. 生成自由变形数据
    - 拉丁超立方
4. 根据设计数据生成不同模型
    - 使用sculptor对船底进行变形
    - 使用Geomagic Studio进行逆向工程将stl格式转换为stp格式
    - 处理转换后的模型
5. 在形同条件下进行仿真得到仿真结果，将仿真结果目标值与原始设计数据作为训练数据
    - 仿真条件
        速度，两相流分层，波浪长高
    - 工具
        Fluent

## 代理模型
1. 传统代理模型
    - 多项式响应面
        二次响应面
    - 径向基(插值/神经网络模型)
    - [克里金](https://www.baidu.com/link?url=7qj5Am_KCUWF9Xea3AW4Ap8Kg1VYlY1x3G6JzpBe00TmvV84h_Bh059awI4M343d&wd=&eqid=baf4f58b000a9300000000035db64e2d)
        无法使用
        
2. 机器学习方法(回归模型)
    - LinearRegression
    - Ridge
    - Lasso
    - RandomForestRegressor
    - GradientBoostingRegressor
    - SVR
    - LinearSVR
    - ElasticNet
    - SGDRegressor
    - BayesianRidge
    - KernelRidge
    - ExtraTreesRegressor
    - XGBRegressor
    - AdaBoostRegressor
    - BaggingRegressor
    - DecisionTreeRegressor
    - KNeighborsRegressor

## 选定代理模型 [代码完成]
1. 训练各模型选取其中最佳的5个模型
2. 使用网格搜索策略获得模型的最佳参数
3. 使用集成学习方法训练融合模型
    - 选取融合模型(回归函数)
4. 获得融合模型的最佳参数

## 多目标优化
- 各优化算法比较 [地址](https://www.zhihu.com/question/29762576)
- 遗传算法
    已完成代码
- 蚂蚁群算法
- 退火模拟算法

## 验证
- 优化结果验证分析