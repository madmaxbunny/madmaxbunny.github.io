---
title: "Function pointer"
date: 2010-01-09 15:59:22 +0900
categories: ["기타"]
tags: ["function", "function pointer", "pointer"]
---

> 💡 **TL;DR (핵심 요약)**  
> Function pointer에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

Function pointer 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
