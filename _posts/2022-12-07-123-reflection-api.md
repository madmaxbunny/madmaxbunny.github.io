---
title: "Reflection API"
date: 2022-12-07 00:11:07 +0900
categories: ["프로그래밍", "JAVA"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> Reflection API에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

Reflection API 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
