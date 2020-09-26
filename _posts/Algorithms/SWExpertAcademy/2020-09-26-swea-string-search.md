---
title: "[SW아카데미] 파이썬 S/W 문제해결 응용 - 문자열 탐색"
tags: 알고리즘 SW아카데미
---

## 문자열 탐색

*<https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYM1Ca240DFAVT>*

### 공통 단어 검색

*Problem No.**5252***

``` python
for tc in range(1, int(input())+1):
    lenA, lenB = map(int, input().split())
    A, B = set(), set()

    for _ in range(lenA):
        A.add(input())
    for _ in range(lenB):
        B.add(input())

    print("#{} {}".format(tc, len(A&B)))
```

### 접두어 검색

*Problem No.**5253***

``` python
for tc in range(1, int(input())+1):
    lenA, lenB = map(int, input().split())
    A, B = [], []

    for _ in range(lenA):
        A.append(input())
    for _ in range(lenB):
        B.append(input())
    
    count = 0
    for prefix in B:
        for string in A:
            if prefix == string[:len(prefix)]:
                count += 1
                break

    print("#{} {}".format(tc, count))
```

### 부분 문자열

*Problem No.**5254***

| *매우 쉽게 풀고 메모리 오류*

``` python
for tc in range(1, int(input())+1):
    N, string = input().split()
    N = int(N)
    subset = set()

    for i in range(1, len(string) + 1):
        for j in range(len(string) + 1 - i):
            subset.add(string[j: j + i])

    subset_list = sorted(list(subset))
    print("#{} {} {}".format(tc, subset_list[N-1][0], len(subset_list[N-1])))
```

|*솔직히 말하면 이거 이해 잘 안됨<br>ref: <https://daep93.github.io/2020/04/10/SW-5254/>*

``` python
def calc_lcp(A, B):
    min_len = min(len(A), len(B))

    for c in range(min_len):    # A와 B를 비교해, 처음부터 연속된 같은 글자의 수가 LCP
        if A[:c + 1] != B[:c + 1]:
            break
    return c

def find_n_th_substring(suffix, n, max_len):
    lcp = 0
    i = 0

    while i < len(suffix):
        cur_idx, cur_suffix = suffix[i]
        candidate_num = max_len - cur_idx
        
        if candidate_num - lcp >= n:
            return cur_suffix[:n+lcp]
        else:
            n -= candidate_num - lcp
            if i != len(suffix) - 1:
                lcp = calc_lcp(cur_suffix, suffix[i+1][1])
            i += 1
    return 0, 0

for tc in range(1, int(input())+1):
    N, string = input().split()
    N = int(N)
    
    suffix_unordered = [(i, string[i:]) for i in range(len(string))]
    suffix_ordered = sorted(suffix_unordered, key = lambda x: x[1])

    prefix = find_n_th_substring(suffix_ordered, N, len(string))
    print("#{} {} {}".format(tc, prefix[0], len(prefix)))
```

|*Suffix와 LCP가 잘 이해 안돼서 다시 만들어보는 중<br>중복을 체크해야하는데.... 다시 공부하자.....*

``` python
for tc in range(1, int(input())+1):
    N, string = input().split()
    N = int(N)
    
    suffix_list = sorted([(i, string[i:]) for i in range(len(string))], key = lambda x: x[1])
    print(suffix_list)

    lcp = [0]*len(string)
    for i in range(1, len(string)):
        min_len = min(len(suffix_list[i-1][1]), len(suffix_list[i][1]))
        c = 0
        while c < min_len:
            if suffix_list[i-1][1][:c+1] != suffix_list[i][1][:c+1]:
                break
            c += 1
        lcp[i] = c
    print(lcp)
```