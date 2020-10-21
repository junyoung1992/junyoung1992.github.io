---
title: "[프로그래머스] SQL - GROUP BY - 3 - 입양 시각 구하기(1)"
tags: SQL
---

## 입양 시각 구하기(1)

*<https://programmers.co.kr/learn/courses/30/lessons/59412>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT
FROM     ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING   HOUR>=9 AND HOUR<=19
ORDER BY HOUR
```