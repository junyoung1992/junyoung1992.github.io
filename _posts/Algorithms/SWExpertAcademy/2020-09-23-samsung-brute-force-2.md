---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 완전 검색 - 전자카트"
tags: 알고리즘 SW아카데미
---

## 전자카트

### 문제 내용

골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

<img src="/assets/posts/algorithms/SWExpertAcademy/bf-2.png">

이 경우 최소 소비량은 89가 된다.

### 입력

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

### 출력

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

### 입출력 예시

|---
|입력|출력|
|---
|3<br>3<br>0 18 34<br>48 0 55<br>18 7 0<br>4<br>0 83 65 97<br>82 0 78 6<br>19 19 0 82<br>6 34 94 0<br>5<br>0 9 26 85 42<br>14 0 84 31 27<br>58 88 0 16 46<br>83 61 94 0 17<br>40 71 24 38 0|#1 89<br>#2 96<br>#3 139|

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