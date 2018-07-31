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
    count = 0

    for idx in input :
        idx = int(idx)

        if idx == 8 :
            count += 1

        else :
            pass

    return count


if __name__ == '__main__' :
    total_sum = 0

    for i in range(10001) :
        total_sum += sol(i)

    print(total_sum)
