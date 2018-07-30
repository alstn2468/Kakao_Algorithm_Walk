# 001.py
x = [100, 200, 300, 400]
y = [10, 20, 30, 40]

def double(x) : return x * 2

print(max(x))
print(min(x))
print(len(x))
print(type(x))
print(dir(x))
print(sum(x))
print(list(map(double, x)))
'''
400
100
4
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
1000
[200, 400, 600, 800]
'''

z = list(zip(x, y))
for i, j in z :
    print(i, j)
'''
100 10
200 20
300 30
400 40
'''

for i, j in enumerate(x, 100) :
    print(i ,j)

'''
100 100
101 200
102 300
103 400
'''
