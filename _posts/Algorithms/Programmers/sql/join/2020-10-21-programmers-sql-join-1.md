---
title: "[프로그래머스] SQL - JOIN - 1 - 없어진 기록 찾기"
tags: SQL 프로그래머스
---

## 없어진 기록 찾기

*<https://programmers.co.kr/learn/courses/30/lessons/59042>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT  ANIMAL_ID, NAME
FROM    ANIMAL_OUTS
WHERE   ANIMAL_ID
        NOT IN (
            SELECT ANIMAL_ID
            FROM ANIMAL_INS
        )
```