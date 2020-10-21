---
title: "[프로그래머스] Summer/Winter Coding(2019) - 2 - 지형 이동"
tags: 알고리즘 Python3 프로그래머스 UNSOLVED
---

## 지형 이동

*<https://programmers.co.kr/learn/courses/30/lessons/62050>*

### 문제 설명

N x N 크기인 정사각 격자 형태의 지형이 있습니다. 각 격자 칸은 1 x 1 크기이며, 숫자가 하나씩 적혀있습니다. 격자 칸에 적힌 숫자는 그 칸의 높이를 나타냅니다.

이 지형의 아무 칸에서나 출발해 모든 칸을 방문하는 탐험을 떠나려 합니다. 칸을 이동할 때는 상, 하, 좌, 우로 한 칸씩 이동할 수 있는데, 현재 칸과 이동하려는 칸의 높이 차가 height 이하여야 합니다. 높이 차가 height 보다 많이 나는 경우에는 사다리를 설치해서 이동할 수 있습니다. 이때, 사다리를 설치하는데 두 격자 칸의 높이차만큼 비용이 듭니다. 따라서, 최대한 적은 비용이 들도록 사다리를 설치해서 모든 칸으로 이동 가능하도록 해야 합니다. 설치할 수 있는 사다리 개수에 제한은 없으며, 설치한 사다리는 철거하지 않습니다.

각 격자칸의 높이가 담긴 2차원 배열 land와 이동 가능한 최대 높이차 height가 매개변수로 주어질 때, 모든 칸을 방문하기 위해 필요한 사다리 설치 비용의 최솟값을 return 하도록 solution 함수를 완성해주세요.

### 제한사항

* land는 N x N크기인 2차원 배열입니다.
* land의 최소 크기는 4 x 4, 최대 크기는 300 x 300입니다.
* land의 원소는 각 격자 칸의 높이를 나타냅니다.
* 격자 칸의 높이는 1 이상 10,000 이하인 자연수입니다.
* height는 1 이상 10,000 이하인 자연수입니다.

### 입출력 예

|---
|land|height|result|
|---
|[[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]|3|15|
|[[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]|1|18|

#### 입출력 예 설명

**입출력 예 # 1**

각 칸의 높이는 다음과 같으며, 높이차가 3 이하인 경우 사다리 없이 이동이 가능합니다.

<img src="https://grepp-programmers.s3.amazonaws.com/files/production/c08b7af3db/5efe34cb-1e69-4474-8e0f-b6929184ebdd.png" width="400px">

위 그림에서 사다리를 이용하지 않고 이동 가능한 범위는 같은 색으로 칠해져 있습니다. 예를 들어 (1행 2열) 높이 4인 칸에서 (1행 3열) 높이 8인 칸으로 직접 이동할 수는 없지만, 높이가 5인 칸을 이용하면 사다리를 사용하지 않고 이동할 수 있습니다.

따라서 다음과 같이 사다리 두 개만 설치하면 모든 칸을 방문할 수 있고 최소 비용은 15가 됩니다.

* 높이 5인 칸 → 높이 10인 칸 : 비용 5
* 높이 10인 칸 → 높이 20인 칸 : 비용 10

**입출력 예 # 2**

각 칸의 높이는 다음과 같으며, 높이차가 1 이하인 경우 사다리 없이 이동이 가능합니다.

<img src="https://grepp-programmers.s3.amazonaws.com/files/production/5bfffc0d72/af5db829-8ea1-4f4c-a5a8-ed11e029d135.png" width="400px">

위위 그림과 같이 (2행 1열) → (1행 1열), (1행 2열) → (2행 2열) 두 곳에 사다리를 설치하면 설치비용이 18로 최소가 됩니다.

### 코드

*일단 각 영역을 분리했는데... 최단 거리는??*

``` python
from collections import deque
import math

def bfs(x, y, N, land, visited, height, group):
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    queue = deque([[x, y]])
    
    while queue:
        x, y = queue.popleft()
        visited[y][x] = group
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < N) and (0 <= ny < N) and \
               (visited[ny][nx] == 0) and (abs(land[ny][nx] - land[y][x]) <= height):
                    visited[ny][nx] = group
                    queue.append([nx, ny])

def solution(land, height):
    answer = 0
    N = len(land)
    visited = [[0] * N for _ in range(N)]
    
    # land 그룹 지정
    group = 1
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                bfs(x, y, N, land, visited, height, group)
                group += 1
    
    print(visited)
    
    return answer
```