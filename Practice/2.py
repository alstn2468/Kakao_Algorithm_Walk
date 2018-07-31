input = input().split()

t = int(input[0])
del input[0]

check_neg = False

if t < 0 :
    t = abs(t)
    check_neg = True

if check_neg :
    for t in range(t) :
        input.insert(0, input[-1])
        del input[-1]

else :
    for _ in range(t) :
        input.append(input[0])
        del input[0]

print('Result : ', end = '')

for i in range(len(input)) :
    if i is len(input) - 1 :
        print(input[i])

    else :
        print(input[i], end = ' ')
