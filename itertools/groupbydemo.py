from itertools import groupby
from operator import itemgetter

data = [
    {'name': 'zhangsan', 'age': 20, 'country': 'China'},
    {'name': 'lisi', 'age': 19, 'country': 'USA'},
    {'name': 'wangwu', 'age': 22, 'country': 'JP'},
    {'name': 'zhaoliu', 'age': 21, 'country': 'USA'},
    {'name': 'maqi', 'age': 22, 'country': 'USA'},
    {'name': 'yangba', 'age': 18, 'country': 'China'}
]
data1 = sorted(data, key=itemgetter('country'))
for country, gp in groupby(data1, key=itemgetter('country')):
    for g in gp:
        print('%s%s' % (country, g))

out = dict([(key, len(list(group))) for key, group in groupby(data1, key=itemgetter('country'))])
print(out)
