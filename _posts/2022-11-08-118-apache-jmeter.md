---
title: Apache Jmeter
date: 2022-11-08 23:50:03 +0900
categories:
- 프로그래밍
- 기타
tags:
- jmeter
- 부하테스트
---

> **[핵심 요약]**
> Apache Jmeter 작업에 대해 실무에서 검증된 핵심 설정 및 처리 방법을 정돈해둔 노트이에요.

---

## 1. 개요 및 배경

Apache Jmeter에 관해 개발 및 인프라 운용 과정에서 접했던 내용들을 공유해볼게요.

---

## 2. 핵심 설명 및 설정 가이드

---

## 1. 개요 및 배경

---

## 2. 핵심 설명 및 설정 가이드

>  **TL;DR (핵심 요약)**  
> Apache Jmeter에 대한 상세 설명 및 핵심 가이드이에요.

---

## 1. 개요 및 배경

Apache Jmeter 가이드 및 실무 적용 설명이에요.

---

## 2. 핵심 설명 및 설정 가이드

### **1\. 설치**

1) [https://jmeter.apache.org](https://jmeter.apache.org/) 에서 다운로드 (아래는 apache-jmeter-5.5)

2) 압축 해제 후 bin > jmeter.bat 실행

* * *

### **2\. Thread Group**

\- 하나의 테스트 실행 단위

![](/assets/img/posts/img_118_01.png)

1) Number of Threads (user) : 가상 사용자 수

2) Ramp-up period (second) : 전체 가상 사용자 유입 시간 (테스트 실행 후 모든 사용자가 접속해야하는 시간)

* Number of Threads : 6, Ramp-up period : 60 

→ 60초 안에 6명의 가상 사용자를 만들어야 한다. (즉, 평균 10초마다 가상 유저가 생성됨을 의미)

3) Loop Count : 테스트 반복 횟수

* Number of Threads : 100, Ramp-up period : 10, Loop Count : 5

→ 100명의 유저가 0.1초마다 접속하며 각 유저마다 5번씩 실행한다.

* * *

### **3\. HttpRequest**

\- Add > Sampler > Http Request

\- 기본 Http 테스트

![](/assets/img/posts/img_118_02.png)

\- 이미지와 같이 Protocol(https), Server Name, Paths 작성

\- 하단에 Get 파라미터의 Name과 Value를 정의할 수 있으며, ${emp_id} 형태로 변수 지정 가능

* * *

### **4\. 멀티 파라미터 사용하기**

\- Add > Config Element > CSV Data Set Config 

\- HTTP 호출할 때마다 CSV 또는 TXT에 저장한 변수를 차례로 바꿔가며 호출 가능하다.

![](/assets/img/posts/img_118_03.png)

1) Filename : 파일 경로

\- txt 파일로 가능하며, 각 데이터 마다 엔터로 구분 가능하다.

![](/assets/img/posts/img_118_04.png)

2) Variable Name : 파일에서 읽은 값을 담을 변수명

3) Delimiter : 파일에서 한 줄에 여러 값이 있을 때 사용하는 구분자

* * *

### **5\. 쿠키 사용하기**

\- Add > Config Element > HTTP Cookie Manager 

\- 생성만 하면 해당 Thread Group에 쿠키가 적용된다. (별도 조치 불필요)

\- 테스트에 로그인 로직 등 쿠기가 필요한 경우 사용하면 좋다.

![](/assets/img/posts/img_118_05.png)

* * *

### **6\. Listener**

\- 테스트 결과를 그래프 또는 보고서 형태로 추출

추천 Listener

1) Summary Report

2) Response Time Graph

3) View Results in Table

**4) View Results Tree**

![](/assets/img/posts/img_118_06.png)

---

## 3. 정리하며

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.

---

## 3. 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있으시다면 언제든 댓글로 편하게 말씀해주세요.
