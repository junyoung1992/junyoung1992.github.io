---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 완전 검색 - 2 - 전자카트"
tags: 알고리즘 SW아카데미
---

## 전자카트

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT>*

### 코드

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