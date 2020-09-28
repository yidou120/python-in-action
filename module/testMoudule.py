# as 模块名的别名
# import mymoudule as md
# md.printName("xxx")
# from 导入模块部分代码
from mymoudule import printName
printName("xxx")
from mymoudule import person
print(person["name"])
print(person.get("age"))
import platform
print(platform.system())
# 平台模块中的所有名称
print(dir(platform))