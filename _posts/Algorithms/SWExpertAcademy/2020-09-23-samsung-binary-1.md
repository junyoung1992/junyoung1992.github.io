---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 시작하기 - 1 - 이진수"
tags: 알고리즘 SW아카데미
---

## 이진수 1

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT>*

### 코드

``` python
HEXA_DEC = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for i in range(1, int(input()) + 1):
    _, hex = input().split()
    answer = ""
    for n in hex:
        if '0' <= n <= '9': temp = int(n)
        else: temp = HEXA_DEC[n]
        compare = 8
        for _ in range(4):
            if temp & compare: answer += "1"
            else: answer += "0"
            compare >>= 1
    print("#{} {}".format(i, answer))
```