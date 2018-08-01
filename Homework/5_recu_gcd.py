# 5_recu_gcd.py
def sol(num1, num2) :
    if num2 == 0 :
        return num1

    else :
        return sol(num2, num1 % num2)


print(sol(12, 6))
'''
6
'''
print(sol(144, 12))
'''
12
'''
