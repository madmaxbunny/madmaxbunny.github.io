---
title: "Android setDoInput GET/POST 이슈"
date: "2022-11-19T16:09:32+09:00"
category: "프로그래밍/Android"
tags: ["android", "Get", "Post", "setDoInput"]
original_url: "https://priv.tistory.com/120"
tistory_id: 120
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
    
