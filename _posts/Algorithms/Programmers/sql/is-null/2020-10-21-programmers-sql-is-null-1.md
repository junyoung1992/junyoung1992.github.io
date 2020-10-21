---
title: "[프로그래머스] SQL - IS NULL - 1 - 이름이 없는 동물의 아이디"
tags: SQL 프로그래머스
---

## 이름이 없는 동물의 아이디

*<https://programmers.co.kr/learn/courses/30/lessons/59039>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   ANIMAL_ID
FROM     ANIMAL_INS
WHERE    NAME IS NULL
ORDER BY ANIMAL_ID ASC
```