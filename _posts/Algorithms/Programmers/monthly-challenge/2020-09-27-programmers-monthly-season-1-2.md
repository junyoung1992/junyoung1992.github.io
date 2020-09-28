---
title: "[프로그래머스] 월간 코드 챌린지 시즌 1 - 2 - 삼각 달팽이"
tags: 알고리즘 Python3 프로그래머스
---

## 삼각 달팽이

*<https://programmers.co.kr/learn/courses/30/lessons/68645>*

### 문제 설명

정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e1e53b93-dcdf-446f-b47f-e8ec1292a5e0/examples.png" width="400px">

### 제한사항

* n은 1 이상 1,000 이하입니다.

### 입출력 예

|---
|n|result|
|---
|4|[1,2,9,3,10,8,4,5,6,7]|
|5|[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]|
|6|[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]|

### 코드

``` python
from itertools import chain

def get_next(x, y, D):
    DELTA = {'D': (0, 1), 'R': (1, 0), 'U': (-1, -1)}
    dx, dy = DELTA[D][0], DELTA[D][1]
    return x+dx, y+dy

def check_turn(next_x, next_y, n, answer):
    return next_x > next_y or next_y < 0 or next_y >= n or answer[next_y][next_x] != 0

def solution(n):
    NEXT = {'D': 'R', 'R': 'U', 'U': 'D'}
    N = sum(range(1, n+1))
    answer = [[0] * i for i in range(1, n+1)]
    
    cur_x, cur_y, cur_D = 0, 0, 'D'
    for num in range(1, N+1):
        answer[cur_y][cur_x] = num

        if check_turn(*get_next(cur_x, cur_y, cur_D), n, answer):
            cur_D = NEXT[cur_D]
            
        cur_x, cur_y = get_next(cur_x, cur_y, cur_D)
        
    return list(chain(*answer))
```