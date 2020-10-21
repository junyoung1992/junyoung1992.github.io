---
title: "[프로그래머스] SQL - IS NULL - 3 - NULL 처리하기"
tags: SQL
---

## NULL 처리하기

*<https://programmers.co.kr/learn/courses/30/lessons/59410>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM     ANIMAL_INS
ORDER BY ANIMAL_ID ASC
```