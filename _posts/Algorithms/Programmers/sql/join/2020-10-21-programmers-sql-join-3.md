---
title: "[프로그래머스] SQL - JOIN - 3 - 오랜 기간 보호한 동물(1)"
tags: SQL 프로그래머스
---

## 오랜 기간 보호한 동물(1)

*<https://programmers.co.kr/learn/courses/30/lessons/59044>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   NAME, DATETIME
FROM     ANIMAL_INS
WHERE    ANIMAL_ID
         NOT IN (
             SELECT ANIMAL_ID
             FROM ANIMAL_OUTS
         )
ORDER BY DATETIME ASC
LIMIT    3
```