---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 시작하기 - 2 - 이진수"
tags: 알고리즘 SW아카데미
---

## 이진수 2

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT>*

### 코드

``` python
for i in range(1, int(input())+1):
    number = float(input())
    divide = 1
    answer = ''
    for _ in range(12):
        divide *= 0.5
        if number - divide >= 0:
            answer += '1'
            number -= divide
            if not number: break
        else:
            answer += '0'
    if number: answer = "overflow"
    print("#{:d} {}".format(i, answer))
```