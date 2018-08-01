# 013.py
'''
x       f(x)        return
5       f(5)        5 * f(4)
4       f(4)        4 * f(3)
3       f(3)        3 * f(2)
2       f(2)        2 * f(1)
1       f(1)        1
'''

def fac_recu(num) :
    if num > 1 :
        return num * fac_recu(num - 1)

    else :
        return 1

print(fac_recu(5))
'''
120
'''
