---
title: "[프로그래머스] Summer/Winter Coding(~2018) - 10 - 쿠키 구입"
tags: 알고리즘 Python3 프로그래머스
---

## 쿠키 구입

*<https://programmers.co.kr/learn/courses/30/lessons/49995>*

### 문제 설명

과자를 바구니 단위로 파는 가게가 있습니다. 이 가게는 1번부터 N번까지 차례로 번호가 붙은 바구니 N개가 일렬로 나열해 놨습니다.

철수는 두 아들에게 줄 과자를 사려합니다. 첫째 아들에게는 l번 바구니부터 m번 바구니까지, 둘째 아들에게는 m+1번 바구니부터 r번 바구니까지를 주려합니다. 단, 두 아들이 받을 과자 수는 같아야 합니다(1 <= l <= m, m+1 <= r <= N). 즉, A[i] 를 i번 바구니에 들어있는 과자 수라고 했을 때, `A[l]+..+A[m] = A[m+1]+..+A[r]` 를 만족해야 합니다.

각 바구니 안에 들은 과자 수가 차례로 들은 배열 cookie가 주어질 때, 조건에 맞게 과자를 살 경우 한 명의 아들에게 줄 수 있는 가장 많은 과자 수를 return 하는 solution 함수를 완성해주세요. (단, 조건에 맞게 과자를 구매할 수 없다면 0을 return 합니다)

### 제한사항

* cookie의 길이는 1 이상 2,000 이하입니다.
* cookie의 각각의 원소는 1 이상 500 이하인 자연수입니다.

### 입출력 예

|---
|cookie|result|
|---
|[1,1,2,3]|3|
|[1,2,4,5]|0|

#### 입출력 예 설명

**입출력 예 # 1**

첫째 아들에게 2, 3번 바구니를, 둘째 아들에게 4번 바구니를 사주면 두 아들은 각각 과자 3개를 받습니다.

**입출력 예 # 2**

주어진 조건에 맞게 과자를 살 방법이 없습니다.

### 코드

``` python
def solution(cookie):
    answer = 0
    N = len(cookie)
    loop_out = False
    
    session = [0, cookie[0]]
    for i in range(1, N):
        session.append(session[i] + cookie[i])
    
    for l in range(0, N):
        for m in range(l+1, N):
            first_son = session[m] - session[l]
            
            if (first_son > session[N] // 2) or \
               (first_son > session[N] - session[m]):
                # 첫째 아들이 전체의 절반 이상을 갖거나
                # 첫째 아들이 둘째 아들이 가질 수 있는 것보다 많이 가질 때
                break
            
            if first_son < answer:
                # 첫째 아들이 현재 구한 최댓값보다 적게 가질 때
                continue
                
            for r in range(m+1, N+1):
                second_son = session[r] - session[m]
                
                if second_son > session[N] // 2:
                    # 둘째 아들이 전체의 절반 이상을 가질 때
                    break
                
                if first_son == second_son:
                    answer = max(answer, first_son)
                    if answer == session[N] // 2:
                        # answer이 가질 수 있는 최댓값
                        loop_out = True
                    break
                elif first_son < second_son:
                    break
            if loop_out:
                break
        if loop_out:
            break
    
    return answer
```