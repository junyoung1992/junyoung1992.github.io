---
title: "[SW아카데미] 파이썬 S/W 문제해결 응용 - 동적계획법의 활용"
tags: 알고리즘 Python3 SW아카데미 UNSOLVED
---

## 동적계획법의 활용

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYODN63DsDFAVT>*

### 정렬된 부분 집합

*Problem No.**5258***

``` python
for tc in range(1, int(input())+1):
    N, *n_list = map(int, input().split())
    len_list = [0] * N

    for i in range(N):
        if i == 0:  # n_list[i]를 마지막으로 하는 부분 집합의 최장 길이는 1
            len_list[i] = 1

        else:
            max_len = 0

            for j in range(i):
                # n_list[i]보다 작은 값 중 가장 큰 값을 마지막 원소로 하는 부분 집합의 최장 길이 탐색
                if n_list[j] < n_list[i] and max_len < len_list[j]:
                    max_len = len_list[j]
            len_list[i] = max_len + 1

    print("#{} {}".format(tc, max(len_list)))
```

### 그래프의 최소 비용

*Problem No.**5260***

``` python

```

### 전기카트 2

*Problem No.**5260***

``` python

```