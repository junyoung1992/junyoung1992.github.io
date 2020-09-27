---
title: "[프로그래머스] 동적계획법 - 4 - 도둑질"
tags: 알고리즘  Python3 프로그래머스
---

## 도둑질

*<https://programmers.co.kr/learn/courses/30/lessons/42897>*

### 문제 설명

도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.

<img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/e7dd4f51c3/a228c73d-1cbe-4d59-bb5d-833fd18d3382.png" width="400px">

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

### 제한사항

* 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
* money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

### 입출력 예

|---
|money|return|
|---
|[1,2,3,1]|4|

### 코드

``` python
def solution(money):
    steal_first = [0] * len(money)
    steal_first[0] = money[0]
    steal_first[1] = steal_first[0]
    
    steal_not_first = [0] * len(money)
    steal_not_first[1] = money[1]
    
    for i in range(2, len(money)):
        steal_first[i] = max(steal_first[i-1], steal_first[i-2] + money[i])
        steal_not_first[i] = max(steal_not_first[i-1], steal_not_first[i-2] + money[i])
    return max(max(steal_first[0:-1]), max(steal_not_first))
```