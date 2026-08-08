---
title: '[UNIX] makefile'
date: 2014-01-03 09:43:18 +0900
categories:
- 프로그래밍
- System
tags: []
---

[UNIX] makefile에 대한 정리 노트이에요. 참고하시는 데 도움되었으면 해요.

---

## 개요 및 배경

[UNIX] makefile에 관해 실무와 개발 과정에서 알게 된 핵심 내용들을 공유해요.

---

## 핵심 설명 및 코드

>  **TL;DR (핵심 요약)**  
> [UNIX] makefile에 대한 상세 설명 및 핵심 가이드이에요.

---

## 개요 및 배경

[UNIX] makefile 가이드 및 실무 적용 설명이에요.

---

## 핵심 설명 및 코드

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

## 정리하며

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.

---

## 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.
