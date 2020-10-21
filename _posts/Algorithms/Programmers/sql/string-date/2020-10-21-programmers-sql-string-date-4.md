---
title: "[프로그래머스] SQL - String, Date - 4 - 오랜 기간 보호한 동물(2)"
tags: SQL
---

## 오랜 기간 보호한 동물(2)

*<https://programmers.co.kr/learn/courses/30/lessons/59411>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   A.ANIMAL_ID, A.NAME
FROM     ANIMAL_INS AS A
         INNER JOIN ANIMAL_OUTS AS B
         ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY B.DATETIME - A.DATETIME DESC
LIMIT    2
```