---
title: "[프로그래머스] SQL - String, Date - 2 - 이름에 el이 들어가는 동물 찾기"
tags: SQL
---

## 이름에 el이 들어가는 동물 찾기

*<https://programmers.co.kr/learn/courses/30/lessons/59047>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   ANIMAL_ID, NAME
FROM     ANIMAL_INS
WHERE    NAME LIKE "%el%" AND ANIMAL_TYPE = "Dog"
ORDER BY NAME
```