---
title: "MY-SQL"
date: "2022-11-02T23:50:49+09:00"
category: "프로그래밍/DB"
tags: []
original_url: "https://priv.tistory.com/115"
tistory_id: 115
---

### **1\. 계정생성**
    
    
    ```sql
    create user '계정아이디'@'%' identified by '비밀번호';
    ```
    

host를 '%' 로 주면 모든 외부 IP에서 접속할 수 있다.

### **2\. 계정조회**
    
    
    ```sql
    select host, user, password from user;
    ```
    

### **3\. DB 생성**
    
    
    ```sql
    create schema testDB;
    use testDB;
    ```
    

### **4\. 권한부여**

[1. 계정생성] 이후 아래 쿼리 수행
    
    
    ```bash
    grant all privileges on '스키마명'.'테이블명' to '계정명'@'호스트' 
    identified by '계정비밀번호' with grant option;
    
    -- Select 권한만 부여
    grant select privileges on testDB.* to '계정명'@'%';
    
    -- 권한 적용
    flush privileges;
    ```
    

* * *

1\. ERROR 1410 (42000): You are not allowed to create a user with GRANT

> [1. 계정생성] 생성 후 [4.권한부여] 실행 시 해결함
