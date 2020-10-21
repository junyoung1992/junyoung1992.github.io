---
title: "[프로그래머스] SQL - String, Date - 1 - 루시와 엘라 찾기"
tags: SQL
---

## 루시와 엘라 찾기

*<https://programmers.co.kr/learn/courses/30/lessons/59046>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM   ANIMAL_INS
WHERE  NAME
       IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")
```