---
title: "[프로그래머스] 월간 코드 챌린지 시즌 1 - 3 - 풍선 터트리기"
tags: 알고리즘 Python3 프로그래머스
---

## 풍선 터트리기

*<https://programmers.co.kr/learn/courses/30/lessons/68645>*

### 문제 설명

일렬로 나열된 n개의 풍선이 있습니다. 모든 풍선에는 서로 다른 숫자가 써져 있습니다. 당신은 다음 과정을 반복하면서 풍선들을 단 1개만 남을 때까지 계속 터트리려고 합니다.

1. 임의의 **인접한** 두 풍선을 고른 뒤, 두 풍선 중 하나를 터트립니다.
2. 터진 풍선으로 인해 풍선들 사이에 빈 공간이 생겼다면, 빈 공간이 없도록 풍선들을 중앙으로 밀착시킵니다.

여기서 조건이 있습니다. 인접한 두 풍선 중에서 **번호가 더 작은 풍선**을 터트리는 행위는 최대 1번만 할 수 있습니다. 즉, 어떤 시점에서 인접한 두 풍선 중 번호가 더 작은 풍선을 터트렸다면, 그 이후에는 인접한 두 풍선을 고른 뒤 번호가 더 큰 풍선만을 터트릴 수 있습니다.

당신은 어떤 풍선이 최후까지 남을 수 있는지 알아보고 싶습니다. 위에 서술된 조건대로 풍선을 터트리다 보면, 어떤 풍선은 최후까지 남을 수도 있지만, 어떤 풍선은 무슨 수를 쓰더라도 마지막까지 남기는 것이 **불가능**할 수도 있습니다.

일렬로 나열된 풍선들의 번호가 담긴 배열 a가 주어집니다. 위에 서술된 규칙대로 풍선들을 1개만 남을 때까지 터트렸을 때 최후까지 남기는 것이 가능한 풍선들의 개수를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

* a의 길이는 1 이상 1,000,000 이하입니다.
    * `a[i]`는 i+1 번째 풍선에 써진 숫자를 의미합니다.
    * a의 모든 수는 -1,000,000,000 이상 1,000,000,000 이하인 정수입니다.
    * a의 모든 수는 서로 다릅니다.

### 입출력 예

|---
|a|result|
|---
|[9,-1,-5]|3|
|[-16,27,65,-2,58,-92,-71,-68,-61,-33]|6|

### 코드

*효율성 망했어... 다시 풀자*

``` python
def solution(a):
    answer = len(a)
    if answer == 1:
        return 1
    elif answer == 2:
        return 2
    
    # 가장 왼쪽의 원소와 가장 오른쪽의 원소는 항상 가능
    for i, num in enumerate(a[1:-1], 1):
        left = min(a[:i])
        right = min(a[i+1:])
        
        # 왼쪽 원소들의 최소값과 오른쪽 원소들의 최소값이
        # 모두 해당 원소보다 작으면 해당 원소는 남길 수 없음
        # 좌 우, 둘 중 하나는 가운데 원소보다 커야 가운데 원소를 남길 수 있다
        if left < num and num > right:
            answer -= 1
    return answer
```

*그래서 다시 풀었다*

``` python
def solution(a):
    answer = 0
    find = [{"left": 0, "right": 0} for _ in range(len(a))]

    MAX_LEFT = float("inf")
    MAX_RIGHT = float("inf")

    # 각 a[i]에 대한 left 최솟값 탐색 (a[i] 포함)
    for i, num in enumerate(a):
        if num < MAX_LEFT:
            MAX_LEFT = num
        find[i]["left"] = MAX_LEFT
    
    # 각 a[i]에 대한 right 최솟값 탐색 (a[i] 포함)
    for i, num in reversed(list(enumerate(a))):
        if num < MAX_RIGHT:
            MAX_RIGHT = num
        find[i]["right"] = MAX_RIGHT
    
    for i, num in enumerate(a):
        if num == find[i]["left"] or num == find[i]["right"]:
            answer += 1
        
    return answer
```