# 011.py
from collections import deque

data = input('회전수, 문자열 입력 : ').split()

result = deque(data[1:])
result.rotate(int(data[0]))

print(' '.join(result))
