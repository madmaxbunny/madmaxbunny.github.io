---
title: Http Connection pool
date: 2022-07-09 01:18:34 +0900
categories:
- 프로그래밍
- JAVA
tags: []
---
> **[핵심 요약]**
> Http Connection pool의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

## 1. 개요 및 배경

Http Connection pool은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

## 2. 핵심 설명 및 코드

> Http Connection pool의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

Http Connection pool은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

> Http Connection pool 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

Http Connection pool과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

자바에서 많이 쓰는 HTTP 통신 라이브라리

1\. HttpURLConnection (자바 기본)

2\. HttpClient (Apache 제공)

### **1\. HttpURLConnection**

\- 가벼움.

\- 단일 Connection을 제공하므로 만약 1개의 URL만 반복해서 호출하는 구조라면 HttpClient보다 성능이 우수

\- 3 way handshake 과정이 최초 1번만 발생하기 때문에 HttpClient보다 2-3배는 빠른 통신이 가능하다.

### **2\. HttpClient**

\- 다양한 기능. 무겁다.

\- Connection pool 제공

\- Connection pool을 컨트롤하지 못하면 HTTP 통신마다 3 way handshake가 발생하며 HttpURLConnection보다 느리다.

\- 특히, 국내 서버-해외 클라이언트 등 물리적 거리가 먼 환경에서 3 way handshake 발생 여부는 성능상 큰 차이가 발생함 

### **3\. HttpClient Connection pool 사용 방법**

#### **1) 기본**

\- 각 통신마다 동일한 Connection pool 객체를 사용해야 함 (당연히..)

\- 그래서 Spring DI 또는 싱글톤 패턴으로 PoolingHttpClientConnectionManager 생성 필요

\- 또한 pool에서 주기적으로 Connection을 제거하는 로직을 직접 구현해야함 (안그러면 계속 쌓임..)

\- 참고 : <https://www.hyoyoung.net/103>

#### **2) NTCredentials 등 서버 인증을 사용하는 통신**

\- 위 3-1) 방식 만으로는 connection 재사용 불가 (계속 pool에 쌓이기만함..)

\- 아래와 같은 추가 조치 필요
    
    
```java
CookieStore cookieStore = new BasicCookieStore();
HttpClientContext httpContext = HttpClientContext.create();
httpContext.setCookieStore(cookieStore);
...
response = httpClient.execute(httpPost, httpContext); // execute 함수에 HttpClientContext 반드시 추가
```
    

Test 버전 : httpclient-4.3.5.jar, httpclient-4.4.1.jar

---

---

이상으로 Http Connection pool의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 Http Connection pool의 기초 개념과 실행 방법에 대한 공유를 마칩니다.
