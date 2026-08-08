---
title: '[UNIX] makefile'
date: 2014-01-03 09:43:18 +0900
categories:
- 프로그래밍
- System
tags: []
---
> **[핵심 요약]**
> [UNIX] makefile의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

## 1. 개요 및 배경

[UNIX] makefile은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

## 2. 핵심 설명 및 코드

> [UNIX] makefile의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

[UNIX] makefile은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

> [UNIX] makefile 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[UNIX] makefile과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

```
msh : libmsh.o msh_main.o 
 gcc -o msh libmsh.o msh_main.o 
libmsh.o : libmsh.c libmsh.h 
 gcc -c libmsh.c 
msh_main.o : libmsh.c libmsh.h 
 gcc -c msh_main.c 
clean: 
 rm *.o

```
    

Eaxmple 
    
    
```
dstest : mylist.o myqueue.o member_info.o stock_reserv.o dstest_main.o 
 gcc -o dstest mylist.o myqueue.o member_info.o stock_reserv.o dstest_main.o 
mylist : mylist.c mylist.h 
 gcc -c dstest_main.c 
myqueue : myqueue.c myqueue.h 
 gcc -c myqueue.c 
member_info : member_info.c member_info.h 
 gcc -c member_info.c 
stock_reserv : stock_reserv.c stock_reserv.h 
 gcc -c stock_reserv.c 
dstest_main : dstest_main.c stock_reserv.h member_info.h myqueue.c mylist.h 
 gcc -c dstest_main.c 
clean :   
 rm *.o

```

---

---

이상으로 [UNIX] makefile의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [UNIX] makefile의 기초 개념과 실행 방법에 대한 공유를 마칩니다.
