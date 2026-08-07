---
title: "memset(), strcpy() 동적 배열의 초기화와 복사"
date: "2010-01-09T15:55:17+09:00"
category: "프로그래밍/C/C++"
tags: []
original_url: "https://priv.tistory.com/24"
tistory_id: 24
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
