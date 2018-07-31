'''
1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라
8이라는 숫자를 모두 카운팅 해야 한다.
ex) 8808 - 3
    8888 - 4
'''

a = 8808
b = 8888

def sol(input) :
    input = str(input)

    return input.count('8')


if __name__ == '__main__' :
    total_sum = 0

    print('- Solution Method Test -')
    print(sol(8), sol(88), sol(888), sol(8888))
    print(sol(80), sol(880), sol(8880))
    '''
    - Solution Method Test -
    1 2 3 4
    1 2 3
    '''


    for i in range(10001) :
        total_sum += sol(i)

    print('- From 1 to 10,000 each 8 count solution -')
    print(total_sum)
    '''
    - From 1 to 10,000 each 8 count solution -
    4000
    '''
