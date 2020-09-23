---
title: "[SW아카데미] 파이썬 S/W 문제해결 구현 - 시작하기 - 2 - 이진수"
tags: 알고리즘 SW아카데미
---

## 이진수 2

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT>*

### 문제 내용

0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

N = 0.625
0.101 (이진수)
= 1\*$2^-1$ + 0\*$2^-2$ + 1\*$2^-3$
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

### 입력

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N이 주어진다.

### 출력

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

### 입출력 예시

|---
|입력|출력|
|---
|3<<br>0.625<br>0.1<br>0.125|#1 101<br>#2 overflow<br>#3 001|

### 코드

``` python
for i in range(1, int(input())+1):
    number = float(input())
    divide = 1
    answer = ''
    for _ in range(12):
        divide *= 0.5
        if number - divide >= 0:
            answer += '1'
            number -= divide
            if not number: break
        else:
            answer += '0'
    if number: answer = "overflow"
    print("#{:d} {}".format(i, answer))
```