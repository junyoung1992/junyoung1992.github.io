---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 백트래킹"
tags: 알고리즘 SW아카데미
---

## 백트래킹

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT>*

### 전기버스2

``` python
def DFS(idx):
    global count, temp

    if idx >= N - 1:    # 목적지에 도착하면
        if count > temp:    # temp와 기존에 저장한 count를 비교
            count = temp
        return

    if count < temp: return # temp가 더 높으면 탐색 종료
    
    start, battery_life = idx, batteries[start]

    for i in range(start+battery_life, start, -1):  # 도착한 곳에서 무조건 배터리 충전
        temp += 1   # DFS
        DFS(i)
        temp -= 1   # Back Tracking

for tc in range(1, int(input())+1):
    N, *batteries = map(int, input().split())
    count, temp = N, 0

    DFS(0)

    print("#{} {}".format(tc, count - 1)) # 출발지에서 배터리 충전은 세지 않음
```

### 퀵 정렬

``` python
def DFS(idx):
    global visited, temp, answer

    if idx == N:    # 마지막까지 확인
        if temp < answer:   # temp가 더 작으면
            answer = temp
        return
    
    if temp > answer: return    # temp가 더 높으면 탐색 종료

    for i in range(N):
        if visited[i]:  # 이미 선택한 제품은 지나감
            continue

        visited[i] = True   # DFS
        temp += table[idx][i]
        DFS(idx+1)
        visited[i] = False  # Back Tracking
        temp -= table[idx][i]

for tc in range(1, int(input())+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    answer, temp = 99*N, 0
    visited = [False] * N
    DFS(0)

    print("#{} {}".format(tc, answer))
```