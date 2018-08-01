# 014.py
'''
x       f(x)        return
15      7           1 + bin_fun(7)            -> 1
7       3           1 + 1 + bin_fun(3)        -> 11
3       1           1 + 1 + 1 + bin_fun(1)    -> 111
1       1           1 + 1 + 1 + 1             -> 1111
'''
def bin_fun(input) :
    if input < 2 :
        print(input, end = '')

    else :
        bin_fun(input // 2)
        print(input % 2, end = '')

bin_fun(15)
