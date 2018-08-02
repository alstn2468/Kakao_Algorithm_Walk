# 3_recu_sum.py
def sol(num) :
    if num > 1 :
        return num + sol(num - 1)

    else :
        return 1

print(sol(10))
print(sol(100))
'''
55
5050
'''
