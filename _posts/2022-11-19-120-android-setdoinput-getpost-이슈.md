---
title: "Android setDoInput GET/POST 이슈"
date: 2022-11-19 16:09:32 +0900
categories: ["프로그래밍", "Android"]
tags: ["android", "get", "post", "setdoinput"]
---

> 💡 **TL;DR (핵심 요약)**  
> Android setDoInput GET/POST 이슈에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

Android setDoInput GET/POST 이슈 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
