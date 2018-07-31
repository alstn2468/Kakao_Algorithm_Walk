# 006.py
jeju = {'melon'  : 5000,
        'apple'  : 2500,
        'banana' : 3000,}

print(jeju.get('a', '못찾았음!!'))
'''
못찾았음!!
'''

def week(x) :
    return {0 : 'mon',
            1 : 'tue',
            2 : 'wed',
            3 : 'thr',
            4 : 'fri',
            5 : 'sat',
            6 : 'sun',}.get(x, '못찾았음!!')

print(week(3))
'''
thr
'''
