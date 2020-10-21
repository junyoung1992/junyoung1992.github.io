---
title: "[프로그래머스] SQL - GROUP BY - 2 - 동명 동물 수 찾기"
tags: SQL 프로그래머스
---

## 동명 동물 수 찾기

*<https://programmers.co.kr/learn/courses/30/lessons/59041>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   *
FROM     (
          SELECT   NAME, COUNT(NAME) AS COUNT
          FROM     ANIMAL_INS
          GROUP BY NAME
         ) SQ1
WHERE    COUNT >= 2
ORDER BY NAME ASC
```