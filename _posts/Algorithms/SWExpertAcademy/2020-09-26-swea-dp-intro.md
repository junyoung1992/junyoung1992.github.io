---
title: "[SW아카데미] 파이썬 S/W 문제해결 응용 - 동적계획법의 소개"
tags: 알고리즘 Python3 SW아카데미
---

## 동적계획법의 소개

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNNbK29EDFAVT>*

### 타일 붙이기

*Problem No.**5255***

``` python
for tc in range(1, int(input())+1):
    N = int(input())
    f = [1] * (N+1)
    f[1] = 1
    f[2] = 3

    for i in range(3, N + 1):
        f[i] = f[i-1] + f[i - 2] * 2 + f[i - 3]
    
    print("#{} {}".format(tc, f[N]))
```

### 이항계수

*Problem No.**5256***

``` python
for tc in range(1, int(input())+1):
    N, x, y = map(int, input().split())
    coef = [[0] * (N+1) for _ in range(N+1)]

    coef[0][0] = 1
    for i in range(1, N+1):
        coef[i][0] = coef[i-1][0]
        for j in range(1, i):
            coef[i][j] = coef[i-1][j-1] + coef[i-1][j]
        coef[i][i] = coef[i-1][i-1]
    
    print("#{} {}".format(tc, coef[N][N-x]))
```