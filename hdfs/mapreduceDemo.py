from functools import reduce
initList = ['a','bb','cc']
# map将list中的每个元素执行len函数 返回值也为一个list
mapResult = map(len,initList)
outList = list(mapResult)
print(outList)
# for result in list(mapResult):
#     print(result)
# reduce将结果的每一项进行累加
out = reduce(lambda x,y:x+y,outList)
print(type(mapResult))
print(out)
