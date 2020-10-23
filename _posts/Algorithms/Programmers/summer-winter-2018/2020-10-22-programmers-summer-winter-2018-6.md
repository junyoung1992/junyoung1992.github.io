---
title: "[프로그래머스] Summer/Winter Coding(~2018) - 6 - 방문 길이"
tags: 알고리즘 Python3 프로그래머스
---

## 방문 길이

*<https://programmers.co.kr/learn/courses/30/lessons/49994>*

### 문제 설명

게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

* U: 위쪽으로 한 칸 가기
* D: 아래쪽으로 한 칸 가기
* R: 오른쪽으로 한 칸 가기
* L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

<img src="https://res.cloudinary.com/jistring93/image/upload/v1495542181/%EB%B0%A9%EB%AC%B8%EA%B8%B8%EC%9D%B41_qpp9l3.png" width="400px">

예를 들어, ULURRDLLU로 명령했다면

<img src="https://res.cloudinary.com/jistring93/image/upload/v1495542443/%EB%B0%A9%EB%AC%B8%EA%B8%B8%EC%9D%B42_lezmdo.png" width="400px">

* 1번 명령어부터 7번 명령어까지 다음과 같이 움직입니다.

<img src="https://res.cloudinary.com/jistring93/image/upload/v1495542704/%EB%B0%A9%EB%AC%B8%EA%B8%B8%EC%9D%B43_sootjd.png" width="400px">

* 8번 명령어부터 9번 명령어까지 다음과 같이 움직입니다.

<img src="https://res.cloudinary.com/jistring93/image/upload/v1495542767/%EB%B0%A9%EB%AC%B8%EA%B8%B8%EC%9D%B44_hlpiej.png" width="400px">

이때, 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다. 예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다. (8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다)

단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

예를 들어, LULLLLLLU로 명령했다면

<img src="https://res.cloudinary.com/jistring93/image/upload/v1495545063/%EB%B0%A9%EB%AC%B8%EA%B8%B8%EC%9D%B45_nitjwj.png" width="400px">

* 1번 명령어부터 6번 명령어대로 움직인 후, 7, 8번 명령어는 무시합니다. 다시 9번 명령어대로 움직입니다.

<img src="https://res.cloudinary.com/jistring93/image/upload/v1495544946/%EB%B0%A9%EB%AC%B8%EA%B8%B8%EC%9D%B46_nzhumd.png" width="400px">

이때 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.

명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

### 제한사항

* dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
* dirs의 길이는 500 이하의 자연수입니다.

### 입출력 예

|---
|dirs|answer|
|---
|"ULURRDLLU"|7|
|"LULLLLLLU"|7|

#### 입출력 예 설명

**입출력 예 # 1**

문제의 예시와 같습니다.

**입출력 예 # 2**

문제의 예시와 같습니다.

### 코드

``` python
DIRECTION = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

def solution(dirs):
    answer = 0
    x, y = 0, 0
    route = set()
    
    for dir in dirs:
        dx, dy = DIRECTION[dir]
        nx, ny = x+dx, y+dy
        
        if -5<=nx<=5 and -5<=ny<=5:
            if ((x, y), (nx, ny)) not in route:
                route.add(((x, y), (nx, ny)))
                route.add(((nx, ny), (x, y)))
                answer += 1
            x, y = nx, ny
    
    return answer
```