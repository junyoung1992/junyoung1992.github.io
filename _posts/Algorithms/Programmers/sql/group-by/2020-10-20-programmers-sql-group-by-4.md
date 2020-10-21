---
title: "[프로그래머스] SQL - GROUP BY - 4 - 입양 시각 구하기(2)"
tags: SQL 프로그래머스
---

## 입양 시각 구하기(2)

*<https://programmers.co.kr/learn/courses/30/lessons/59413>*

### 문제 설명

### 예시

### 코드

*갑자기 변수를 선언함*

``` sql
-- 코드를 입력하세요
SET @hour := -1;

SELECT (@hour := @hour + 1) AS HOUR,
       (SELECT COUNT(DATETIME)
        FROM   ANIMAL_OUTS
        WHERE  HOUR(DATETIME)=@HOUR
       ) AS COUNT
FROM   ANIMAL_OUTS
WHERE  @hour<23
```