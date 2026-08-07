---
title: "[PL/SQL] PL/SQL 시작하기"
date: "2014-01-03T09:33:25+09:00"
category: "프로그래밍/DB"
tags: []
original_url: "https://priv.tistory.com/44"
tistory_id: 44
---

**1\. PL/SQL 이란?  
** \- SQL + 절차적 언어(Procedural Language) 기능 추가  
\- Oracle의 표준 데이터 액세스 언어  
\- 성능 향상  
\- 모듈식 프로그램 개발  
\- 예외처리 가능  
(- Oracle SQL Developer를 사용할 경우, 코드 작성 후 F5를 눌러 실행)  
  
**2.****변수  
** \- 변수 이름 규칙은 Oracle SQL 과 동일  
\- 변수유형  
1) 스칼라형(Scalar) : 자바의 프리미티브 타입  
ex) CHAR(10), DATE, ...  
2) 조합형(Composite) : 자바의 레퍼런스 타입   
ex) recode  
  
**2\. PL/SQL BLOCK의 종류  
** \- BLOCK : C언어의 함수와 같은 기능  


1) 익명 블록
    
    
    ```
    [DECLARE] 
     
    BEGIN 
      --statments; 
    [EXCEPTION] 
    END;
    
    ```
    

2) 프로시저 블록
    
    
    ```
    PROCEDURE name 
    IS 
    BEGIN 
      --statments; 
    [EXCEPTION] 
    END;
    
    ```
    

3) 함수 블록
    
    
    ```
    FUNCTION name 
    RETURN datatype 
    IS 
    BEGIN 
      --statments; 
      RETURN value; 
    [EXCEPTION] 
    END;
    
    ```
    

hello world 출력하기
    
    
    ```
    set serveroutput on -- 스크린버퍼를 활성화 
    BEGIN 
         dbms_output.put_line('Hello world'); 
    END;
    
    ```
    
