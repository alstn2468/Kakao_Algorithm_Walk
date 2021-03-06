# 018.py
def get_min_idx(list) :
    idx = 0

    for i in range(1, len(list)) :
        if list[i] < list[idx] :
            idx = i

    return idx

def InsertionSort(list) :
    result = []

    while list :
        temp = get_min_idx(list)
        min = list.pop(temp)
        result.append(min)

    return result

list = [1, 3, 2, 5, 4, 7, 6, 9, 8]

print('- Before Sorting -')
print(list)
'''
- Before Sorting -
[1, 3, 2, 4, 5, 7, 6, 9, 8]
'''

list = InsertionSort(list)

print('- After Sorting -')
print(list)
'''
- After Sorting -
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
