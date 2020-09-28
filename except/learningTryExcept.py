try:
    x = 1
    print(x)
except NameError:
    print("未定义变量出现错误")
except:
    print("其他错误")
else:
    print("没问题")
finally:
    print("执行完毕")
'''
未定义变量出现错误
执行完毕
'''
'''
1
没问题
执行完毕
'''