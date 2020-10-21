---
title: "[프로그래머스] SQL - JOIN - 2 - 있었는데요 없었습니다"
tags: SQL
---

## 있었는데요 없었습니다

*<https://programmers.co.kr/learn/courses/30/lessons/59043>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT      B.ANIMAL_ID, B.NAME
FROM        ANIMAL_INS A
            INNER JOIN ANIMAL_OUTS B
            ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE       A.DATETIME > B.DATETIME
ORDER BY    A.DATETIME
```