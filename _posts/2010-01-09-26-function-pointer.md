---
title: Function pointer
date: 2010-01-09 15:59:22 +0900
categories:
- 카테고리 없음
tags: []
---
> **[핵심 요약]**
> C언어에서 함수 주소를 포인터 배열에 저장하여 사칙연산을 동적으로 호출하는 함수 포인터 활용법입니다.

---

## 1. 개요 및 배경

Function pointer은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> Function pointer의 기본 개념과 실무 적용 명령어를 

---

Function pointer은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> Function pointer 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

Function pointer과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

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

---

이상으로 Function pointer의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 Function pointer의 기초 개념과 실행 방법에 대한 공유를 마칩니다.