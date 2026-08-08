---
title: Android setDoInput GET/POST 이슈
date: 2022-11-19 16:09:32 +0900
categories:
- 프로그래밍
- Android
tags: []
---
> **[핵심 요약]**
> 안드로이드 HttpURLConnection 전송 시 setDoInput 및 GET/POST 메서드 호출 순서 오류 조치법입니다.

---

## 1. 개요 및 배경

Android setDoInput GET/POST 이슈은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

## 2. 핵심 설명 및 코드

> Android setDoInput GET/POST 이슈의 기본 개념과 실무 적용 명령어를 

---

Android setDoInput GET/POST 이슈은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 

---

> Android setDoInput GET/POST 이슈 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

Android setDoInput GET/POST 이슈과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

**아래 코드를 실행하면 GET과 POST 중 어떤 방식으로 발송이 될까?**
    
    
```java
URL url = new URL(CALL_SEVER_URL);
conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("GET");
conn.setRequestProperty("Cache-Control", "no-cache");
conn.setRequestProperty("Content-Type", "application/json");
conn.setRequestProperty("Accept", "application/json");
conn.setConnectTimeout(TIME_OUT);
conn.setReadTimeout(TIME_OUT);
conn.setDoInput(true); 	
conn.setDoOutput(true); // InputStream으로 서버로부터 응답을 받겠다는 옵션

int resCode = conn.getResponseCode();
```
    

### **테스트 결과**

1) PC 자바에서는 GET 방식으로 발송한다. 

2) Android 자바에서는 POST 방식으로 발송한다. 

그래서 Android에서 **GET 방식으로 전송하기 위해서는 반드시 setDoInput(false)로 사용** 해야한다.
    
    
```java
conn.setDoInput(false); // OutputStream으로 POST 데이터를 넘겨주겠다는 옵션
```

---

---

이상으로 Android setDoInput GET/POST 이슈의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 Android setDoInput GET/POST 이슈의 기초 개념과 실행 방법에 대한 공유를 마칩니다.