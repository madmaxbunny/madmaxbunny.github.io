---
title: "[JAVA] GCM Sender and Library"
date: 2014-01-03 09:50:15 +0900
categories: ["프로그래밍", "JAVA"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> [JAVA] GCM Sender and Library에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

[JAVA] GCM Sender and Library 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

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

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
