---
title: "[프로그래머스] SQL - String, Date - 3 - 중성화 여부 파악하기"
tags: SQL 프로그래머스
---

## 중성화 여부 파악하기

*<https://programmers.co.kr/learn/courses/30/lessons/59049>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
       CASE
           WHEN SEX_UPON_INTAKE LIKE "%Neutered%" OR SEX_UPON_INTAKE LIKE "%Spayed%"
                THEN "O"
           ELSE
                "X"
        END AS "중성화"
FROM  ANIMAL_INS
```