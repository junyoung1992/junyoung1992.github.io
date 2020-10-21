---
title: "[프로그래머스] SQL - String, Date - 5 - DATETIME에서 DATE로 형 변환"
tags: SQL
---

## DATETIME에서 DATE로 형 변환

*<https://programmers.co.kr/learn/courses/30/lessons/59414>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d") AS "날짜"
FROM     ANIMAL_INS
ORDER BY ANIMAL_ID
```