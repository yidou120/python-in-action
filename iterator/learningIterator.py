list = ("11","22","33")
myit = iter(list)
print(next(myit))
print(next(myit))
print(next(myit))
# for i in myit:
#     print(i)

# 定义一个迭代器
class myIterator:
    def __iter__(self):
        self.number = 1
        return self
    def __next__(self):
        if(self.number<10):
            x = self.number
            self.number += 1
            return x
        else:
            raise StopIteration

testIter = myIterator()
for i in iter(testIter):
    print(i)
