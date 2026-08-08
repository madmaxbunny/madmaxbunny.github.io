---
title: "memset(), strcpy() 동적 배열의 초기화와 복사"
date: 2010-01-09 15:55:17 +0900
categories: ["프로그래밍", "C"]
tags: []
---

> **[핵심 요약]**
> memset(), strcpy() 동적 배열의 초기화와 복사 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

## 1. 개요 및 배경

memset(), strcpy() 동적 배열의 초기화와 복사과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

## 2. 핵심 설명 및 코드

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

## 3. 정리하며

