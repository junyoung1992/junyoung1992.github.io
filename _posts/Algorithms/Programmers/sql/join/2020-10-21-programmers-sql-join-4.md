---
title: "[프로그래머스] SQL - JOIN - 4 - 보호소에서 중성화한 동물"
tags: SQL 프로그래머스
---

## 보호소에서 중성화한 동물

*<https://programmers.co.kr/learn/courses/30/lessons/59045>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM   ANIMAL_INS A
       INNER JOIN ANIMAL_OUTS B
       ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE  A.SEX_UPON_INTAKE != B.SEX_UPON_OUTCOME
```