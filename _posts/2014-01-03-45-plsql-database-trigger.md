---
title: "[PL/SQL] Database Trigger"
date: 2014-01-03 09:34:32 +0900
categories: ["프로그래밍", "DB"]
tags: []
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
    
