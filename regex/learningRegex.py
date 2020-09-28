import re
txt = "The rain in Spain"
# search
result = re.search('^The.*Spain$',txt)
# 17
print("len:"+str(len(txt)))
# <re.Match object; span=(0, 17), match='The rain in Spain'>
print("result:"+str(result))
# 返回匹配的起始索引 是一个元组 span
print("span:"+str(result.span()))
# 返回文本中匹配的部分 group
print("group:"+str(result.group()))
# string属性 返回传递给search的文本
print("string:"+str(result.string))
# 匹配空白字符 返回匹配的第一个 如不存在返回None值
# <re.Match object; span=(3, 4), match=' '>
result1 = re.search('\s',txt)
# None
result2 = re.search('fafa',txt)
print("result1:"+str(result1))
print("result2:"+str(result2))
# findall 返回匹配项的所有列表
result3 = re.findall('\s',txt)
# [' ', ' ', ' ']
print("result3:"+str(result3))
# split 以匹配参数分割 返回列表
result4 = re.split('\s',txt)
# 第三个参数代表在第几次匹配时 分割字符串
result5 = re.split('\s',txt,1)
# ['The', 'rain', 'in', 'Spain']
print("result4:"+str(result4))
# ['The', 'rain in Spain']
print("result5:"+str(result5))
# sub 将匹配项替换为参数文本
result6 = re.sub('\s','-',txt)
# result6:The-rain-in-Spain
print("result6:"+str(result6))
# 替换前两项
result7 = re.sub('\s','=',txt,2)
# result7:The=rain=in Spain
print("result7:"+str(result7))

result8 = re.search(r'\bS\w+',txt)
s1 = result8.string
s2 = result8.span()
s3 = result8.group()
print("string:"+s1,"span:"+str(s2),"group:"+s3)