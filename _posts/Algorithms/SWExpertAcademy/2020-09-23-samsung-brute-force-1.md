---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 완전 검색 - 1 - 최소합"
tags: 알고리즘 SW아카데미
---

## 최소합

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT>*

### 코드

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