# import numpy as np
# import pandas as pd
# import random

# dataSet =pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
# dataSet.head()
# def randSplit(dataSet, rate):
#     l = list(dataSet.index) #提取出索引
#     random.shuffle(l) #随机打乱索引
#     dataSet.index = l #将打乱后的索引重新赋值给原数据集
#     n = dataSet.shape[0] #总行数
#     m = int(n * rate) #训练集的数量
#     train = dataSet.loc[range(m), :] #提取前m个记录作为训练集
#     test = dataSet.loc[range(m, n), :] #剩下的作为测试集
#     dataSet.index = range(dataSet.shape[0]) #更新原数据集的索引
#     test.index = range(test.shape[0]) #更新测试集的索引
#     return train, test

# def gnb_classify(train,test):
#     labels = train.iloc[:,-1].value_counts().index #提取训练集的标签种类
#     mean =[] #存放每个类别的均值
#     std =[] #存放每个类别的方差
#     result = [] #存放测试集的预测结果
#     for i in labels:
#         item = train.loc[train.iloc[:,-1]==i,:] #分别提取出每一种类别
#         m = item.iloc[:,:-1].mean() #当前类别的平均值
#         s = np.sum((item.iloc[:,:-1]-m)**2)/(item.shape[0]) #当前类别的方差
#         mean.append(m) #将当前类别的平均值追加至列表
#         std.append(s) #将当前类别的方差追加至列表
#     means = pd.DataFrame(mean,index=labels) #变成DF格式，索引为类标签
#     stds = pd.DataFrame(std,index=labels) #变成DF格式，索引为类标签
#     for j in range(test.shape[0]):
#         iset = test.iloc[j,:-1].tolist() #当前测试实例
#         iprob = np.exp(-1*(iset-means)**2/(stds*2))/(np.sqrt(2*np.pi*stds)) #正态分布公式
#         prob = 1 #初始化当前实例总概率
#         for k in range(test.shape[1]-1): #遍历每个特征
#             prob *= iprob[k] #特征概率之积即为当前实例概率
#             cla = prob.index[np.argmax(prob.values)] #返回最大概率的类别
#         result.append(cla)
#     test['predict']=result
#     acc = (test.iloc[:,-1]==test.iloc[:,-2]).mean() #计算预测准确率
#     print(f'模型预测准确率为{acc}')
#     return test

# for i in range(20):#测试20次，对比测试成功的概率
#     train,test = randSplit(dataSet,0.8)
#     gnb_classify(train,test)
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# 定义训练数据
data_str = """
5.1  3.5  1.4  0.2
4.9  3.0  1.4  0.2
4.7  3.2  1.3  0.2
4.6  3.1  1.5  0.2
5.0  3.6  1.4  0.2
5.4  3.9  1.7  0.4
4.6  3.4  1.4  0.3
5.1  3.4  1.5  0.2
4.4  2.9  1.4  0.2
4.9  3.1  1.5  0.1
4.6  3.7  1.5  0.2
4.8  3.4  1.6  0.2
4.8  3.0  1.4  0.1
4.3  3.0  1.1  0.1
5.8  4.0  1.2  0.2
5.7  4.4  1.5  0.4
5.4  3.9  1.3  0.4
5.1  3.5  1.4  0.3
5.7  3.8  1.7  0.3
5.1  3.8  1.5  0.3
5.4  3.4  1.7  0.2
5.1  3.7  1.5  0.4
4.6  3.6  1.0  0.2
5.1  3.3  1.7  0.5
4.8  3.4  1.9  0.2
5.0  3.0  1.6  0.2
5.0  3.4  1.6  0.4
5.2  3.5  1.5  0.2
5.2  3.4  1.4  0.2
4.7  3.2  1.6  0.2
"""

# 将字符串数据转换为二维NumPy数组
data_list = [list(map(float, line.split())) for line in data_str.strip().split("\n")]
data_matrix = np.array(data_list)

new_data_str = """
7.0  3.2  4.7  1.4
6.4  3.2  4.5  1.5
6.9  3.1  4.9  1.5
5.5  2.3  4.0  1.3
6.5  2.8  4.6  1.5
5.7  2.8  4.5  1.3
6.3  3.3  4.7  1.6
4.9  2.4  3.3  1.0
6.6  2.9  4.6  1.3
5.2  2.7  3.9  1.4
5.0  2.0  3.5  1.0
5.9  3.0  4.2  1.5
6.0  2.2  4.0  1.0
6.1  2.9  4.7  1.4
5.6  2.9  3.9  1.3
6.7  3.1  4.4  1.4
5.6  3.0  4.5  1.5
5.8  2.7  4.1  1.0
6.2  2.2  4.5  1.5
5.6  2.5  3.9  1.1
5.9  3.2  4.8  1.8
6.1  2.8  4.0  1.3
6.3  2.5  4.9  1.5
6.1  2.8  4.7  1.2
6.4  2.9  4.3  1.3
6.6  3.0  4.4  1.4
6.8  2.8  4.8  1.4
6.7  3.0  5.0  1.7
6.0  2.9  4.5  1.5
5.7  2.6  3.5  1.0
"""

# 将字符串数据转换为二维NumPy数组
new_data_list = [list(map(float, line.split())) for line in new_data_str.strip().split("\n")]
new_data_matrix = np.array(new_data_list)
# M1_data = np.array([[0, 0, 0], [1, 0, 1], [0, 0, 1], [0, 1, 1]])
# M2_data = np.array([[1, 0, 0], [1, 1, 0], [0, 1, 0], [1, 1, 1]])
M1_data = data_matrix
M2_data = new_data_matrix
# 合并数据
X_train = np.concatenate((M1_data, M2_data), axis=0)

# 定义类别标签
y_train = np.array([0] * len(M1_data) + [1] * len(M2_data))

# 创建LDA模型
lda = LinearDiscriminantAnalysis()

# 拟合模型
lda.fit(X_train, y_train)

# 打印权重向量和截距
print("权重向量:", lda.coef_)
print("截距:", lda.intercept_)

# 定义新的数据点
new_data = np.array([
    [4.8 , 3.1 , 1.6 , 0.2],
    [5.4 , 3.4 , 1.5 , 0.4],
    [5.2 , 4.1 , 1.5 , 0.1],
    [5.5 , 4.2 , 1.4 , 0.2],
    [4.9 , 3.1 , 1.5 , 0.2],
    [5.0 , 3.2 , 1.2 , 0.2],
    [5.5 , 3.5 , 1.3 , 0.2],
    [4.9 , 3.6 , 1.4 , 0.1],
    [5.5 , 2.4 , 3.8 , 1.1],
    [5.5 , 2.4 , 3.7 , 1.0],
    [5.8 , 2.7 , 3.9 , 1.2],
    [6.0 , 2.7 , 5.1 , 1.6],
    [5.4 , 3.0 , 4.5 , 1.5],
    [6.0 , 3.4 , 4.5 , 1.6],
    [6.7 , 3.1 , 4.7 , 1.5],
    [6.3 , 2.3 , 4.4 , 1.3],
    [5.6 , 3.0 , 4.1 , 1.3],
    [5.5 , 2.5 , 5.0 , 1.3],
    [5.5 , 2.6 , 4.4 , 1.2],
    [6.1 , 3.0 , 4.6 , 1.4],
    [5.8 , 2.6 , 4.0 , 1.2],
    [5.0 , 2.3 , 3.3 , 1.0],
    [5.6 , 2.7 , 4.2 , 1.3],
    [5.7 , 3.0 , 4.2 , 1.2],
    [5.7 , 2.9 , 4.2 , 1.3],
    [6.2 , 2.9 , 4.3 , 1.3],
    [5.1 , 2.5 , 3.0 , 1.1],
    [5.7 , 2.8 , 4.1 , 1.3]
])

# 使用模型进行预测
predictions = lda.predict(new_data)

# 打印预测结果
for i, prediction in enumerate(predictions):
    print(f"新数据点 {new_data[i]} 的预测类别为: {prediction}")
