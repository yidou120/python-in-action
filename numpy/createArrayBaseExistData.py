import numpy as np
l = b'this is array'
print(type(l))
result = np.frombuffer(l,dtype='S1',count=4)
print(result)
print(type(result))