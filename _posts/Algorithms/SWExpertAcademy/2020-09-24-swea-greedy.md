---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 탐욕 알고리즘"
tags: 알고리즘 Python3 SW아카데미
---

## 탐욕 알고리즘

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT&&>*

### 컨테이너 운반

*Problem No.**5201***

``` python
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    answer = 0
    for i in range(M):
        temp = 0
        for container in containers:
            if trucks[i] >= container and container >= temp:
                temp = container
        if temp != 0:
            containers.remove(temp)
        answer += temp
    
    print("#{:d} {:d}".format(tc, answer))
```

### 화물 도크

*Problem No.**5202***

``` python
for tc in range(1, int(input())+1):
    N = int(input())
    work_time = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: x[1])

    able = [work_time[0]]
    for i in range(1, N):
        if able[-1][1] <= work_time[i][0]:
            able.append(work_time[i])
    
    print("#{} {}".format(tc, len(able)))
```

### 베이비진 게임

*Problem No.**5203***

``` python
class BabyJin:
    def __init__(self):
        self.cards = {}

    def add_card(self, card):
        cards = self.cards

        if card in cards:
            cards[card] += 1
            if cards[card] == 3: return True
        else:
            cards[card] = 1
            if (card - 2 in cards and card - 1 in cards) or \
               (card - 1 in cards and card + 1 in cards) or \
               (card + 1 in cards and card + 2 in cards):
                return True
        return False

for tc in range(1, int(input())+1):
    deck = list(map(int, input().split()))
    pA = BabyJin()
    pB = BabyJin()

    answer = 0
    for i in range(len(deck)):
        if i % 2 == 0 and pA.add_card(deck[i]):
            answer = 1
            break
        if i % 2 == 1 and pB.add_card(deck[i]):
            answer = 2
            break
        
    print("#{} {}".format(tc, answer))
```