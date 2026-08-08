---
title: "memset(), strcpy() 동적 배열의 초기화와 복사"
date: 2010-01-09 15:55:17 +0900
categories: ["프로그래밍", "C"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> memset(), strcpy() 동적 배열의 초기화와 복사에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

memset(), strcpy() 동적 배열의 초기화와 복사 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
