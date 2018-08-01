# 012.py
def fac_iter(num) :
    result = 1

    for i in range(1, num + 1) :
        result *= i

    return result

def fac_recu(num) :
    if num > 1 :
        return num * fac_recu(num - 1)

    else :
        return 1

print(fac_iter(5))
print(fac_recu(5))
