---
title: "[프로그래머스] SQL - SUM, MAX, MIN - 4 - 중복 제거하기"
tags: SQL 프로그래머스
---

## 중복 제거하기

*<https://programmers.co.kr/learn/courses/30/lessons/59408>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT COUNT(*)
FROM   (
        SELECT   NAME
        FROM     ANIMAL_INS
        WHERE    NAME IS NOT NULL
        GROUP BY NAME
       ) SQ1
```