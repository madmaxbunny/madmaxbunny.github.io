---
title: Reflection API
date: 2022-12-07 00:11:07 +0900
categories:
- 프로그래밍
- JAVA
tags: []
---
> **[핵심 요약]**
> Reflection API의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

## 1. 개요 및 배경

Reflection API은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

## 2. 핵심 설명 및 코드

> Reflection API의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

Reflection API은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

> Reflection API 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

Reflection API과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

### **1\. Reflection**

\- Class 타입의 객체를 통해 특정 클래스의 구조(필드, 메소드, 어노테이션 등)를 런타임에 분석할 수 있는 API

\- JVM에서 실행하는 어플리케이션의 런타임 동작을 검사하거나 수정하는 기능이 필요한 프로그램에서 사용

**단점)**

1\. JVM 최적화 수행 불가

2\. 보안 제한?

3\. 불법적인 작업 (private 필드 및 메서드 액서스) 수행 가능 → 부작용 발생할 수 있다.

<https://docs.oracle.com/javase/tutorial/reflect/>

### **2\. Class 객체를 얻는 방법**
    
    
```java
// 인스턴스를 얻을 수 없을 때 사용
Class a = HttpGet.class;
System.out.println(a.getName());

// 인스턴스를 통한 생성
HttpGet h = new HttpGet();
Class b = h.getClass();

// 이름을 통한 생성. but ClassNotFoundException 처리 필요
Class c = Class.forName("test.HttpGet");
```
    

### **3\. 특정 클래스 구조를 분석**
    
    
```java
public class Home {
public int a = 2;
private String b = "Hello Home";
public int windowCnt() {
return 2;
}
}

// Home 클래스의 필드 가져오기
Class home = Home.class;
Arrays.stream(home.getDeclaredFields()).forEach(System.out::println);
```
    

**결과 :**

![](/assets/img/posts/img_123_01.png)

* * *

---

---

이상으로 Reflection API의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 Reflection API의 기초 개념과 실행 방법에 대한 공유를 마칩니다.
