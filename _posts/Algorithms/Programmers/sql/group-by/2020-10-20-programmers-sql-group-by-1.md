---
title: "[프로그래머스] SQL - GROUP BY - 1 - 고양이와 개는 몇 마리 있을까"
tags: SQL 프로그래머스
---

## 고양이와 개는 몇 마리 있을까

*<https://programmers.co.kr/learn/courses/30/lessons/59040>*

### 문제 설명

### 예시

### 코드

``` sql
-- 코드를 입력하세요
SELECT   ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS COUNT
FROM     ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC
```