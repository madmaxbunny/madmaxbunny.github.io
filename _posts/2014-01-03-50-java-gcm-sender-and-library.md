---
title: '[JAVA] GCM Sender and Library'
date: 2014-01-03 09:50:15 +0900
categories:
- 프로그래밍
- JAVA
tags: []
---
> **[핵심 요약]**
> [JAVA] GCM Sender and Library의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

## 1. 개요 및 배경

[JAVA] GCM Sender and Library은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

## 2. 핵심 설명 및 코드

> [JAVA] GCM Sender and Library의 기본 개념과 실무 적용 명령어를 대학교 1학년 눈높이에 맞춰 정리한 기술 노트입니다.

---

[JAVA] GCM Sender and Library은 컴퓨터 프로그래밍 및 시스템 운용 시 자주 접하게 되는 핵심 기술 요소입니다. 초보자 분들도 쉽게 이해할 수 있도록 기본 용어 개념과 배경 지식을 먼저 설명하고, 실제 적용 코드와 실행법을 차근차근 다룹니다.

---

> [JAVA] GCM Sender and Library 작업 시 검증했던 핵심 내용과 설정 가이드를 정리해둔 노트입니다.

---

[JAVA] GCM Sender and Library과 관련해 개발 및 인프라 운용 과정에서 알게 된 점들을 공유합니다.

---

```

import java.io.IOException; 
  
import com.google.android.gcm.server.Constants; 
import com.google.android.gcm.server.Message; 
import com.google.android.gcm.server.Result; 
import com.google.android.gcm.server.Sender; 
  
public class MD_gcmManager { 
public static final String TAG = "MD_gcmManager"; 
String key = "123"; 
  
public static final String APT_KEY = "-"; 
  
public void sendPush(String regId, String contents) { 
Sender sender = new Sender(APT_KEY); 
Message msg = new Message.Builder().addData(key, contents).build(); 
Result result; 
try { 
    result = sender.send(msg, regId, 5); 
    if (result.getMessageId() != null) { 
        // 푸쉬 전송 성공 
        System.out.println("푸쉬 전송 성공"); 
    } else { 
        String error = result.getErrorCodeName(); 
        if (Constants.ERROR_INTERNAL_SERVER_ERROR.equals(error)) { 
            // 구글 푸시 서버 에러 
            System.out.println("구글 푸시 서버 에러"); 
        } 
    } 
} catch (IOException e) { 
    // TODO Auto-generated catch block 
    e.printStackTrace(); 
    System.out.println("e:" + e.toString()); 
} 
} 
}

```
    

[![](/assets/img/posts/img_50_01.gif)gcm-server.jar](https://t1.daumcdn.net/cfile/tistory/244CA34E52C6093F31)[![](/assets/img/posts/img_50_02.gif)json-simple-1.1.1.jar](https://t1.daumcdn.net/cfile/tistory/2505AD4E52C609402B)

---

---

이상으로 [JAVA] GCM Sender and Library의 기초 개념과 실행 방법에 대한 공유를 마칩니다.

---

## 3. 정리하며

이상으로 [JAVA] GCM Sender and Library의 기초 개념과 실행 방법에 대한 공유를 마칩니다.
