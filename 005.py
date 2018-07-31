# 005.py
jeju = {'melon'  : 5000,
        'apple'  : 2500,
        'banana' : 3000,}

print(dir(jeju))
'''
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''

print(jeju.keys())
print(jeju.values())
print(jeju.items())
'''
dict_keys(['melon', 'apple', 'banana'])
dict_values([5000, 2500, 3000])
dict_items([('melon', 5000), ('apple', 2500), ('banana', 3000)])
'''

seoul = jeju.copy()
seoul['banana'] = 100000
print(jeju)
'''
{'melon': 5000, 'apple': 2500, 'banana': 3000}
'''

seoul = jeju
seoul['banana'] = 100000
print(jeju)
'''
{'melon': 5000, 'apple': 2500, 'banana': 100000}
'''
