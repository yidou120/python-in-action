import sys
from itertools import groupby
from operator import itemgetter


def read_mapper_output(file, separator='\t'):
    for line in file:
        #rstrip()默认删除末尾空格
        yield line.rstrip().split(separator, 1)


def main():
    data = read_mapper_output(sys.stdin)
    # [{a,1},{a,1},{b,1}]
    for word, gp in groupby(data, key=itemgetter(0)):
        # 使用了列表生成式 将遍历的每个值作用第一个函数 保存一个list返回
        # 然后使用sum求列表项的和
        num = sum(int(count) for word, count in gp)
        print("%s%s%d" % (word, '\t', num))
if __name__ == '__main__':
    main()