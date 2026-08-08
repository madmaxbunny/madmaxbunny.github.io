---
title: '[PL/SQL] Database Trigger'
date: 2014-01-03 09:34:32 +0900
categories:
- 프로그래밍
- DB
tags: []
---
> **[핵심 요약]**
> 테이블에 INSERT/UPDATE 이벤트 발생 시 자동으로 실행되는 Oracle 데이터베이스 트리거(Trigger) 구현입니다.

---

## 1. 개요 및 배경

[PL/SQL] Database Trigger은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> [PL/SQL] Database Trigger의 기본 개념과 실무 적용 명령어를 

---

[PL/SQL] Database Trigger은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> [PL/SQL] Database Trigger 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[PL/SQL] Database Trigger과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

```

CREATE TABLE dept 
   AS SELECT department_id,department_name, 0 TOT_DEPT_SAL  
FROM departments; 
SQL>ed trigger_test 
create or replace trigger dept_before 
  before insert on dept 
 begin 
  dbms_output.put_line('문장 before trigger가 발생했습니다.'); 
 end; 
/ 
create or replace trigger dept_after 
 after insert on dept 
 begin 
  dbms_output.put_line('문장 After trigger가 발생했습니다.'); 
 end; 
/ 
create or replace trigger dept_row_after 
 after insert on dept 
 for each row 
 begin 
  dbms_output.put_line('행 after trigger가 발행했습니다.'); 
 end; 
/ 
create or replace trigger dept_row_before 
 before insert on dept 
 for each row 
 begin 
  dbms_output.put_line('행 before trigger가 발생했습니다.'); 
 end; 
/

```
    
    
    
```

set serveroutput on 
insert into dept   
   SELECT department_id,department_name,0 FROM departments WHERE ROWNUM <=2;

```

---

---

이상으로 [PL/SQL] Database Trigger의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [PL/SQL] Database Trigger의 기초 개념과 실행 방법에 대한 공유를 마칩니다.