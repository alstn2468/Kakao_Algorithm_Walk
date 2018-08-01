# 015.py
x = 'kimminsu'

print(x[::-1])

def reverse_str(str) :
    if str == '' :
        return None

    else :
        reverse_str(str[1:])
        print(str[0], end = '')

reverse_str('kimminsu')

def print_str_recu(str) :
    if str == '' :
        return None

    else :
        print(str[0], end = '')
        print_str_recu(str[1:])

print_str_recu('kimminsu')
