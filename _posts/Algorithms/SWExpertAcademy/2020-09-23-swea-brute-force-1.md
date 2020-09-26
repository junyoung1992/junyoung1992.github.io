---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 완전 검색"
tags: 알고리즘 SW아카데미
---

## 완전 검색

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT>*

### 최소합

*Problem No.**5188***

``` python
import math

direction = [(1, 0), (0, 1)]

def dfs(x, y, now_sum):
    global min_sum

    now_sum += board[y][x]
    
    if now_sum > min_sum: return

    if x == size-1 and y == size-1:
        min_sum = now_sum
        return
    
    for d in direction:
        next_x, next_y = x + d[0], y + d[1]
        if next_x < size and next_y < size:
            dfs(next_x, next_y, now_sum)

for i in range(1, int(input())+1):
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]
    min_sum = math.inf

    dfs(0, 0, 0)
    print("#{:d} {:d}".format(i, min_sum))
```

### 전자 카트

*Problem No.**5189***

``` python
from itertools import permutations
import math

for i in range(1, int(input())+1):
    length = int(input())
    input_set = [i for i in range(1, length)]
    board = [list(map(int, input().split())) for _ in range(length)]

    min_cost = math.inf
    for p in permutations(input_set):
        now_sum = board[0][p[0]]
        for j in range(len(p)-1):
            now_sum += board[p[j]][p[j+1]]
        now_sum += board[p[-1]][0]

        if now_sum < min_cost:
            min_cost = now_sum
            
    print("#{:d} {:d}".format(i, min_cost))
```