# 028.py
'''
입력
"점수 | 보너스 | [옵션]"으로 이루어진 문자열 3세트
예) 1S2D*3T
점수는 0에서 10사이의 정수이다.
보너스는 S, D, T 중 하나이다.
옵션은 *이나 #중 하나이며, 없을 수도 있다.

출력
3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
예) 37
'''

input = input()
result = []
recent_num_idx = 0

for i in range(len(input)) :
    if input[i].isnumeric() :
        result.append(int(input[i]))
        recent_num_idx += 1

        if input[i + 1].isnumeric() :
            result[recent_num_idx - 1] = int(str(result[recent_num_idx - 1]) + input[i + 1])
            i += 1

    elif input[i] is '#' :
        result[recent_num_idx - 1] = -result[recent_num_idx - 1]

    elif input[i] is '*' :
        for i in range(0, recent_num_idx) :
            result[i] = result[i] * 2

    elif input[i] is 'S' :
        pass

    elif input[i] is 'D' :
        result[recent_num_idx - 1] = result[recent_num_idx - 1] ** 2

    elif input[i] is 'T' :
        result[recent_num_idx - 1] = result[recent_num_idx - 1] ** 3

print(sum(result))
