---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 그래프의 기본과 탐색"
tags: 알고리즘 SW아카데미
---

## 그래프의 기본과 탐색

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYG3y62EcDFAVT>*

### 연산

``` python
from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    # BFS =======================================
    visited = [False]*1000001   # 1 ~ 1,000,000 까지 체크
    queue = deque()
    queue.append((N, 0))
    visited[N] = True

    while queue:
        q, c = queue.popleft()

        if q == M:
            break

        result = q + 1
        if 0 < result <= 1000000 and not visited[result]:
            # 1,000,000보다 작은 자연수이고 이전에 출력되지 않은 값일 경우
            queue.append((result, c + 1))
            visited[result] = True

        result = q - 1
        if 0 < result <= 1000000 and not visited[result]:
            queue.append((result, c + 1))
            visited[result] = True

        result = q * 2
        if 0 < result <= 1000000 and not visited[result]:
            queue.append((result, c + 1))
            visited[result] = True

        result = q - 10
        if 0 < result <= 1000000 and not visited[result]:
            queue.append((result, c + 1))
            visited[result] = True
    # ===========================================

    print("#{} {}".format(tc, c))
```

### 그룹 나누기

``` python
def find_set(x):    # 모든 하위 원소의 부모를 집합의 루트 원소로 설정
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(A, B):    # 두 집합을 병합
    parent[find_set(A)] = find_set(B)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]

    m_list = list(map(int, input().split()))

    for i in range(M):  # 주어진 쌍 대로 노드 연결
        union(m_list[i*2+1], m_list[i*2])

    answer = []
    for i in range(1, N+1): # 부모 노드로 집합의 루트를 설정하도록 재정리
        answer.append(find_set(i))

    print("#{} {}".format(tc, len(set(answer))))
```