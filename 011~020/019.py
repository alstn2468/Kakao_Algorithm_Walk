# 019.py
def get_insert_idx(result, list) :
    for i in range(0, len(result)) :
        if list < result[i] :
            return i

    return len(result)

def InsertionSort(list) :
    result = []

    while list :
        temp = list.pop(0)
        idx = get_insert_idx(result, temp)
        result.insert(idx, temp)

    return result

list = [1, 3, 2, 4, 5, 7, 6, 9, 8]

print('- Before Sorting -')
print(list)
'''
- Before Sorting -
[1, 3, 2, 4, 5, 7, 6, 9, 8]
'''

print('- After Sorting -')
print(InsertionSort(list))
'''
- After Sorting -
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
