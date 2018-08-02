'''
숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로
바꾸어주는 프로그램을 작성하시오.
단, 프로그래밍 언어에서 지원하는 금액변환 라이브러리는
사용하지 말것
'''
def sol(num) :
    if num[0] == '-' :
        return '-' + sol(num[1:])

    if len(num) <= 3 :
        return num

    if num.find('.') == -1 :
        return sol(num[:-3]) + ',' + num[-3:]

    else :
        return sol(num[:num.find('.')]) + num[num.find('.'):]

num = '12345678'
print(sol(num))

num = '-123456.78'
print(sol(num))

import re

def sol(num):
    return re.sub('(?<=\d)(?=(\d{3})+(?!\d))', ',' ,str(num))

print(sol(-3245.24))
