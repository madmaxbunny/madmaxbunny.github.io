---
title: "Function pointer"
date: 2010-01-09 15:59:22 +0900
categories: ["카테고리 없음"]
tags: []
---

> **[핵심 요약]**
> Function pointer 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트이에요.

---

## 1. 개요 및 배경

Function pointer과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유해요.

---

## 2. 핵심 설명 및 코드

#include <stdio.h>  
#include <string.h>

static int (*table[256])(int,int);

int add(int upper, int under){return upper + under;}  
int sub(int upper, int under){return upper - under;}  
int div(int upper, int under){return upper / under;}  
int mul(int upper, int under){return upper * under;}

void init()  
{  
table['+'] = add;  
table['-'] = sub;  
table['/'] = div;  
table['*'] = mul;  
}

  
int main(int argc, char *argv[]){  
  
int inputA, inputB;  
char operC;

init();  
scanf("%d %c %d", &inputA, &operC, &inputB);  
printf("%d %c %d = %d", inputA, operC, inputB, table[operC](inputA, inputB));

return 0;  
}

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 말씀해주세요.
