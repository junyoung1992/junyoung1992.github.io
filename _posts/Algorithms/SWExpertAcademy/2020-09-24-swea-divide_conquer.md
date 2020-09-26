---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 분할 정복"
tags: 알고리즘 SW아카데미
---

## 분할 정복

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT>*

### 병합 정렬

*Problem No.**5204***

``` python
def merge_sort(arr):
    if len(arr) == 1:
        return arr

    # Divide ==================================================================
    mid = len(arr) // 2
    arr_left = merge_sort(arr[:mid])
    arr_right = merge_sort(arr[mid:])
    
    # Merge ===================================================================
    arr_merge = []
    l = r = 0
    while l < len(arr_left) and r < len(arr_right):
        if arr_left[l] <= arr_right[r]:
            arr_merge.append(arr_left[l])
            l += 1
        else:
            arr_merge.append(arr_right[r])
            r += 1

    global answer
    if arr_left[l:]:    # left가 남은 경우
        arr_merge.extend(arr_left[l:])
        answer += 1
    elif arr_right[r:]: # right가 남은 경우
        arr_merge.extend(arr_right[r:])

    return arr_merge

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    answer = 0
    numbers = merge_sort(numbers)
    print("#{} {} {}".format(tc, numbers[N//2], answer))
```

### 퀵 정렬

*Problem No.**5205***

``` python
def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot + 1, right)

def partition(arr, left, right):
    pivot = (left + right) // 2

    while left < right:
        while left < right and arr[left] < arr[pivot]: left += 1
        while left < right and arr[pivot] <= arr[right]: right -= 1

        if left < right:
            if left == pivot:
                pivot = right
            arr[left], arr[right] = arr[right], arr[left]

    if arr[pivot] < arr[right]:
        arr[pivot], arr[right] = arr[right], arr[pivot]
        pivot = right

    return pivot

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, N-1)
    print("#{} {}".format(tc, numbers[N//2]))
```

### 이진 탐색

*Problem No.**5207***

``` python
def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    flag = None
    while start <= end:
        mid = start + (end - start) // 2
        
        if key == arr[mid]: # 탐색
            return mid
        elif key < arr[mid]:    # 왼쪽
            if flag == "left":  # 왼쪽 연속
                return -1
            end = mid - 1
            flag = "left"
        else:   # 오른쪽
            if flag == "right": # 오른쪽 연속
                return -1
            start = mid + 1
            flag = "right"
    return -1

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    listA = sorted(list(map(int, input().split())))
    listB = list(map(int, input().split()))

    answer = 0
    for b in listB:
        if binary_search(listA, b) != -1:
            answer += 1

    print("#{} {}".format(tc, answer))
```