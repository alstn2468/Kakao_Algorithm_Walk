# 022.py
'''
1차원의 점들이 주어졌을 때,
그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
(단 점들의 배열은 모두 정렬되어있다고 가정한다.)

예를 들어 S = [1, 3, 4, 8, 13, 17, 20]이 주어졌다면,
결과값은 (3, 4)가 될 것이다.
'''
def sol(Input) :
    result = [Input[0], Input[1]]

    for i in range(len(Input) - 1) :
        if Input[i + 1] - Input[i] < result[1] - result[0] :
            result[1], result[0] = Input[i + 1], Input[i]

    return result

if __name__ == '__main__' :
    Input = [1, 3, 4, 8, 13, 17, 20]

    print(sol(Input))
    '''
    [3, 4]
    '''

    pairs = list(zip(Input[0:], Input[1:]))
    pairs.sort(key = lambda x : x[1] - x[0])

    print(pairs[0])
    '''
    (3, 4)
    '''
