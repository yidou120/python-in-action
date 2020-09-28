def myFunction(list):
    for item in list:
        print(item)
myList = ["1","帅哥","美女"]
myFunction(myList)

def myDefaultFunction(city="杭州"):
    print("我在:" + city)
myDefaultFunction("浙江")
myDefaultFunction()

# 递归终止条件 n <= 0
# 递归规律 n-1
def recursionFunction(n):
    if(n>0):
        result = n + recursionFunction(n-1)
    else:
        result = 0
    return result
print(recursionFunction(3))