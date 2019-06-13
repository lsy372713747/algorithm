# -*- coding:utf-8 -*-
"""
快速排序的四种python实现
"""
a = [2,4,5,1,7,9,5,3,6]

#  一行代码实现的简洁版本
quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
        [item for item in array[1:] if item <= array[0]]
    ) + [array[0]] + quick_sort(
        [item for item in array[1:] if item > array[0]]
    )


# 常规实现
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    print(key, "----")
    while left < right:
        print(array)
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        print(array[right])
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
        print(array[left])
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)

quick_sort(a, 0, len(a)-1)
print(a)

# 《算法导论》中的快排程序
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
 
def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1]
    return i + 1

# 用栈实现非递归的快排程序
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])
