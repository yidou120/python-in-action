# python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
# 执行上述命令 安装相关包
import numpy as np
n1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
n2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# 垂直拼接
print(np.vstack((n1,n2)))
# 水平拼接
print(np.hstack((n1,n2)))
# 矩阵之间的算术运算
print("n1+n2\n",n1+n2)
print("n1/n2\n",n1/n2)
print("n1*n2\n",n1*n2)
# 求平方根和标准差
print("sqrt:",np.sqrt(n1))
print("std:",np.std(n1))
# 数组轴的计算
# axis = 0 代表列
# axis = 1 代表行
print("n1列最大的元素:",np.max(n1,axis=0))
print("n1行最小的元素:",np.min(n1,axis=1))
print("每行的和:",np.sum(n1,axis=1))
# 数组切片
# 数组[start:end:step]
print(n1[:2])
print(n1[0:3:2])