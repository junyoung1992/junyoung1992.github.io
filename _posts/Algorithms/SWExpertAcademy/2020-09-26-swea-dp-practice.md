---
title: "[SW아카데미] 파이썬 S/W 문제해결 응용 - 동적계획법의 적용"
tags: 알고리즘 Python3 SW아카데미
---

## 동적계획법의 적용

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNxvq3BIDFAVT>*

### 해피박스

*Problem No.**5258***

``` python
def knapsack(matrix, product, box_size, item_num):
    # 상자 크기가 0이거나 아이템을 0개 선택할 경우를 초기화
    for i in range(item_num + 1):
        matrix[i][0] = 0
    for s in range(box_size + 1):
        matrix[0][s] = 0
    
    for i in range(1, item_num + 1):
        for s in range(1, box_size + 1):
            # 상품의 크기가 가방보다 클 경우, 넣지 못함
            if product[i][0] > s:
                matrix[i][s] = matrix[i-1][s]
            # 작거나 같을 경우, 상품을 넣거나 넣지 않은 것 중 가격이 높은 것을 선택
            else:
                matrix[i][s] = max(matrix[i-1][s - product[i][0]] + product[i][1], matrix[i-1][s])

    return matrix[item_num][box_size]

for tc in range(1, int(input())+1):
    box_size, item_num = map(int, input().split())
    product = list(tuple(map(int, input().split())) for _ in range(item_num))
    
    # 크기 대비 가격을 기준으로 정렬
    product.sort(key = lambda x: x[1]/x[0])
    product.insert(0, (0,0))  # 시작 지점 추가

    matrix = [[-1] * (box_size + 1) for _ in range(item_num + 1)]

    result = knapsack(matrix, product, box_size, item_num)

    print("#{} {}".format(tc, result))
```

### 부분 집합의 합

*Problem No.**5260***

``` python
def partial_sum(K, nums):
    sum_subset = sum(nums)

    if sum_subset < K:
        return 0
    elif sum_subset == K:
        return 1
    else:
        last_num = nums[-1]

        if last_num == K:
            return 1 + partial_sum(K, nums[:-1])
        elif last_num < K:
            return partial_sum(K - last_num, nums[:-1]) + partial_sum(K, nums[:-1])
        else:
            return partial_sum(K, nums[:-1])


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    nums = [i for i in range(1, N+1)]

    result = partial_sum(K, nums)

    print("#{} {}".format(tc, result))
```