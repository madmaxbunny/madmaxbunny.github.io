---
title: '[2009/03/05] 암호학 - Liner Diophantine Equation(선형 디오팔투스 방정식)'
date: 2009-03-09 14:47:41 +0900
categories:
- 프로그래밍
- 기타
tags:
- diophantine
- 디오팔투스
- 암호학
---

[2009/03/05] 암호학 - Liner Diophantine Equation(선형 디오팔투스 방정식)에 대한 정리 노트이에요. 참고하시는 데 도움되었으면 해요.

---

## 개요 및 배경

[2009/03/05] 암호학 - Liner Diophantine Equation(선형 디오팔투스 방정식)에 관해 실무와 개발 과정에서 알게 된 핵심 내용들을 공유해요.

---

## 핵심 설명 및 코드

>  **TL;DR (핵심 요약)**  
> [2009/03/05] 암호학 - Liner Diophantine Equation(선형 디오팔투스 방정식)에 대한 상세 설명 및 핵심 가이드이에요.

---

## 개요 및 배경

[2009/03/05] 암호학 - Liner Diophantine Equation(선형 디오팔투스 방정식) 가이드 및 실무 적용 설명이에요.

---

## 핵심 설명 및 코드

![](/assets/img/posts/img_2_01.png)

  
  
// Subject : Cryptography and Network Security  
// Maker : Lim Kyung-Hyuk  
// Date : 2009/03/05  
// Program : Liner Diophantine Equation(선형 디오팔투스 방정식)   
// Language : Java

import java.io.*;  
public class lde{  
public static void main(String[] ar) throws IOException{  
BufferedReader in = new BufferedReader(new InputStreamReader(System.in));  
  
int a, b, c, d, q, r, a1, b1, c1;  
int r1, r2, s, t, s1 = 1, s2 = 0, t1 = 0, t2 = 1, x, y, x0, y0, k = 0;  
  
System.out.println("Liner Diophantine Equation 'ax + by = c' ");  
System.out.print("input a = ");  
a = Integer.parseInt(in.readLine());  
System.out.print("input b = ");  
b = Integer.parseInt(in.readLine());  
System.out.print("input c = ");  
c = Integer.parseInt(in.readLine());  
System.out.println( a + "x + " + b + "y = " + c);  
System.out.println();

// EA; d=gcd(a,b)  
r1 = a; r2 = b;  
while(r2>0){  
q = r1/r2;  
r = r1 - q * r2;  
r1 = r2; r2 = r;  
}  
d = r1;  
System.out.println(d + " = gcd(" + a +","+ b + ")");  
System.out.println();

// if d|c then TRUE else FALSE and EXIT  
if(0 == d%c){  
System.out.println("d|c is TRUE ");  
}else if(0 == c%d){  
System.out.println("d|c is TRUE ");  
}else{  
System.out.println("d|c is FALSE ");  
System.exit(-1);  
}  
System.out.println();

// The particular  
a1 = a/d;  
b1 = b/d;  
c1 = c/d;  
System.out.println("'a1x + b1y = c1' is '" + a1 + "x + " + b1 + "y = " + c1 + "'");  
System.out.println("'a1s + b1t = 1' is '" + a1 + "s + " + b1 + "t = " + 1 + "'");  
System.out.println();

//// EEA  
r1 = a1; r2 = b1;  
while(r2 > 0){  
q = r1/r2;  
r = r1 - q * r2;  
r1 = r2; r2 = r;

s = s1 - q * s2;  
s1 = s2; s2 = s;

t = t1 - q * t2;  
t1 = t2; t2 = t;  
}  
x0 = (c/d) * s1;  
y0 = (c/d) * t1;  
System.out.println("The particular is x0 = "+ x0 + ", y0 = " + y0);  
System.out.println();

//General  
System.out.println("General is x = " + x0 + " + k(" + b + "/" + d + "), y = " + y0 + " + k(" + a + "/" + d + "), [k is integer]");   
while(k<10){  
x = x0 + k * (b/d);  
y = y0 - k * (a/d);  
k++;

System.out.print("(" + x + ", " + y + "), ");  
}  
System.out.println("...");  
  
}  
}

---

## 정리하며

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.

---

## 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.
