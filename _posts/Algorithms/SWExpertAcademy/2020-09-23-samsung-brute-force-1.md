---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 완전 검색 - 최소합"
tags: 알고리즘 SW아카데미
---

## 최소합

### 문제 내용

그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

<img src="/assets/posts/algorithms/SWExpertAcademy/bf-1.png">

그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

### 입력

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13

### 출력

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

### 입출력 예시

|---
|입력|출력|
|---
|3<br>3<br>1 2 3<br>2 3 4<br>3 4 5<br>4<br>2 4 1 3<br>1 1 7 1<br>9 1 7 10<br>5 7 2 4<br>5<br>6 7 1 10 2<br>10 2 7 5 9<br>9 3 2 9 6<br>1 6 8 2 9<br>8 3 8 2 1|#1 15<br>#2 18<br>#3 33|

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