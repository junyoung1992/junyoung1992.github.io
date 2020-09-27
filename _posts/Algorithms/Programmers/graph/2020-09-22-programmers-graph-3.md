---
title: "[프로그래머스] 그래프 - 3 - 방의 개수"
tags: 알고리즘  Python3 프로그래머스
---

## 방의 개수

*<https://programmers.co.kr/learn/courses/30/lessons/49190>*

### 문제 설명

원점(0,0)에서 시작해서 아래처럼 숫자가 적힌 방향으로 이동하며 선을 긋습니다.

<img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/ec8f232bf0/a47a6c2e-ec84-4bfb-9d4b-ff3ba589b42a.png" width="400px">

ex) 1일때는 `오른쪽 위`로 이동

그림을 그릴 때, 사방이 막히면 방하나로 샙니다.<br>
이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때, 방의 갯수를 return 하도록 solution 함수를 작성하세요.

### 제한사항

* 배열 arrows의 크기는 1 이상 100,000 이하 입니다.
* arrows의 원소는 0 이상 7 이하 입니다.
* 방은 다른 방으로 둘러 싸여질 수 있습니다.

### 입출력 예

|---
|arrows|return|
|---
|[6,6,6,4,4,4,2,2,2,0,0,0,1,6,5,5,3,6,0]|3|

#### 입출력 예 설명

<img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/74fd8df438/22a1ee81-75a6-4220-bd15-6230e35e2931.png" width="400px">

* (0,0) 부터 시작해서 6(왼쪽) 으로 3번 이동합니다. 그 이후 주어진 arrows 를 따라 그립니다.
* 삼각형 (1), 큰 사각형(1), 평행사변형(1) = 3

### 코드

``` python
def solution(arrows):
    d = {0:(0,1),1:(1,1),2:(1,0),3:(1,-1),4:(0,-1),5:(-1,-1),6:(-1,0),7:(-1,1)}
    visited = {(0,0):1}
    edges = {}
    pos = (0,0)
    answer = 0
    
    for a in arrows:
        x, y = d[a]
        
        # 모래시계처럼 교차되는 형태를 고려하기 위해 한 번에 두 칸씩 이동
        for _ in range(2):
            # 좌표 이동
            pos_next = (pos[0]+x,pos[1]+y)

            # 중복 엣지 저장
            edge_1 = (pos, pos_next)
            edges[edge_1] = edges.get(edge_1, 0) + 1
            edge_2 = (pos_next, pos)
            edges[edge_2] = edges.get(edge_2, 0) + 1

            # 해당 노드에 1회 이상 방문했지만, 해당 엣지는 단 한 번만 거쳤을 때 도형 카운트 증가
            visited[pos_next] = visited.get(pos_next, 0) + 1
            if visited[pos_next] > 1 and edges[edge_1] == 1:
                answer += 1
            pos = pos_next
    return answer
```