import camelcase
# 安装 pip install camelcase
# 卸载 pip uninstall camelcase
c = camelcase.CamelCase()
# Long Time No See
txt = "long time no see"
print(c.hump(txt))