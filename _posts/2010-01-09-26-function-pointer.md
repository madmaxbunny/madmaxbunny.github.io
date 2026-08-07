---
title: "Function pointer"
date: 2010-01-09 15:59:22 +0900
categories: ["기타"]
tags: ["function", "function pointer", "pointer"]
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

  

