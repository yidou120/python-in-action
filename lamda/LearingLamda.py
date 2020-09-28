def myFunction(n):
    return lambda i: i*n
# 调用函数 返回一个lamda匿名函数
lambdaFunction = myFunction(3)
# 调用lamda函数
print(lambdaFunction(10))