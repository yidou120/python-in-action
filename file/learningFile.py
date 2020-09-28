f = open('test.txt')
# 默认模式是r read t 文本
# f = open('test.txt','rt')
# 读取所有内容
# print(f.read())
# 读取前10个字符
# print(f.read(10))
# 读取一行
# print(f.readline())
for line in f:
    print(line)
f.close()
print('----------------------------')
# 追加
f1 = open('test1.txt','a')
f1.write('\n')
f1.write('append内容')
f1.close()
# 读取
f2 = open('test1.txt')
for i in f2:
    print(i)
# 覆盖
f3 = open('test2.txt','w')
f3.write('test覆盖')
f3.close()
f4 = open('test2.txt')
print('--------------------------------')
# 读取
for j in f4:
    print(j)
f4.close()
# 创建文件
f5 = open('test3.txt','x')
f5.close()
'''
r – 只读模式，是默认值，如果该文件不存在报错
a – 追加模式，打开文件可以在文件末尾追加内容，如果该文件不存在，则创建该文件
w – 写模式，打开文件写入内容，如果文件不存在，创建该文件
x – 创建文件，创建文件，如果文件存在，返回一个错误
此外，还可以指定该文件以二进制模式还是文本模式处理

t – 文本模式，默认值
b – 二进制模式(例如视频)
'''
