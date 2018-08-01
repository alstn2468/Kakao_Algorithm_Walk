# 4_recu_fib.py
def sol(num) :
    if num > 1 :
        return sol(num - 1) + sol(num - 2)

    else :
        return 1

def fib_list(num) :
    print([sol(n) for n in range(num)], end = '')

fib_list(10)
'''
[1, 1, 2, 3, 5, 8, 13, 21, 34 ,55]
'''
