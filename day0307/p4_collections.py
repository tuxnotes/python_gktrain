from collections import Counter

mystring = ['a','b','c','d','d','d','c','c','e']
cnt = Counter(mystring) # 如果对性能没有太高的要求的话，使用Counter就够了
cnt.most_common(3) # 频率最高的3个值
cnt['b']

# 双向队列
from collections import deque

d = deque('uvw')
d.append('xyz')
d.appendleft('rst')
