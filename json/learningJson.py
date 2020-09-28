import json
x = '{ "name":"杨", "age":38, "city":"Hangzhou"}'
# json字符串转对象dic
result = json.loads(x)
print(result['name'])

# 对象转字符串
y = {
  "name": "哈哈哈",
  "age": 38,
  "city": "Hangzhou"
}
# 默认dumps方法使用ASCII编码中文 要想输出为中文ensure_ascii=False
result1 = json.dumps(y,ensure_ascii=False)
print(result1)

print(json.dumps({"name": "法", "age": 38},ensure_ascii=False))
print(json.dumps(["自行车", "汽车", "高铁"],ensure_ascii=False))
print(json.dumps(("自行车", "汽车", "高铁"),ensure_ascii=False))
print(json.dumps("嘎嘎嘎",ensure_ascii=False))
print(json.dumps(88))
print(json.dumps(95.34))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

z = {
  "name": "发发发发啊",
  "age": 38,
  "married": True,
  "divorced": False,
  "children": ("Alice", "Bob"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Mondeo", "mpg": 24.1}
  ]
}
# indent 缩进几个空格
# separators 分割样式 默认,分割对象 :分割键值对
print(json.dumps(z,indent=4,ensure_ascii=False,separators=(".","=")))