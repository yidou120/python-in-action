import os
pa = os.path
flag = pa.exists('test111.txt')
# <module 'ntpath' from 'C:\\Users\\Jeffrey_Cheng\\AppData\\Local\\Programs\\Python\\Python37\\lib\\ntpath.py'>
print(pa)
# False
print(flag)
if(pa.exists('fafa')):
    os.remove('fafa')
    print('文件存在')
else:
    print('文件不存在')

# 删除文件夹 必须是空
# os.rmdir()