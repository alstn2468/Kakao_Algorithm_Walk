'''
숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로
바꾸어주는 프로그램을 작성하시오.
단, 프로그래밍 언어에서 지원하는 금액변환 라이브러리는
사용하지 말것
'''
def sol(num) :
    result = []

    for i in range(1, len(num) + 1) :
        result.append(num[-i])

        if i % 3 == 0 :
            result.append(',')

    result.reverse()

    if result[0] == ',' :
        del result[0]

    return result

num = '12345678'
print(''.join(sol(num)))
