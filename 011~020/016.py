# 016.py
def get_pos_num(num) :
    if num < 9 :
        print(num, end = '')

        return None

    else :
        print(num % 10, end = '')
        num //= 10
        get_pos_num(num)

        return None

get_pos_num(12345)
