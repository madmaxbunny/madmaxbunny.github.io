---
title: memset(), strcpy() 동적 배열의 초기화와 복사
date: 2010-01-09 15:55:17 +0900
categories:
- 프로그래밍
- C
tags: []
---
> **[핵심 요약]**
> 동적 배열의 메모리를 0으로 초기화하는 memset() 및 문자열을 안전하게 복사하는 strcpy() 함수 활용법입니다.

---

## 1. 개요 및 배경

memset(), strcpy() 동적 배열의 초기화와 복사은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> memset(), strcpy() 동적 배열의 초기화와 복사의 기본 개념과 실무 적용 명령어를 

---

memset(), strcpy() 동적 배열의 초기화와 복사은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> memset(), strcpy() 동적 배열의 초기화와 복사 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

memset(), strcpy() 동적 배열의 초기화와 복사과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

// strcpy(copy본 첫주소, 원본 첫주소).  
// memset(buf, 0, sizeof(buf)), memset(배열이름, 초기화할 문자, sizeof(배열이름))

#include <stdio.h>  
#include <string.h>  
void main(void){

void* a;  
int i=0,cnt = 0;  
char charList[100], copyLsit[100];

scanf("%s",charList);  
  
strcpy(copyLsit, charList);

printf("\n\n\np: %s",copyLsit);

memset(copyLsit, NULL, sizeof(copyLsit));  
printf("\n\n\np: %s",copyLsit);

}

---

---

이상으로 memset(), strcpy() 동적 배열의 초기화와 복사의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 memset(), strcpy() 동적 배열의 초기화와 복사의 기초 개념과 실행 방법에 대한 공유를 마칩니다.