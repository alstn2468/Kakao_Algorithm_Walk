# 020.py
'''
다음과 같은 형태의 배열을
[a1,a2,a3...,an,b1,b2...bn]

다음과 같은 형태로 바꾸시오
[a1,b1,a2,b2.....an,bn]

시간 복잡도 O(n)
공간 복잡도
'''

list = ['a1', 'a2', 'a3', 'an',
        'b1', 'b2', 'b3', 'bn']

result = []

for i in range(len(list) // 2) :
    result.append(list[i])
    result.append(list[i + list.index('b1')])

print(result)

for i in range(len(list)) :
    list.append(list[0][1] + list[0][0])
    list.pop(0)

list.sort()

for i in range(len(list)) :
    list.append(list[0][1] + list[0][0])
    list.pop(0)

print(list)
