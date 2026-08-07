---
title: "[JAVA] GCM Sender and Library"
date: "2014-01-03T09:50:15+09:00"
category: "프로그래밍/JAVA"
tags: []
original_url: "https://priv.tistory.com/50"
tistory_id: 50
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
    

[![](../images/img_50_01.gif)gcm-server.jar](https://t1.daumcdn.net/cfile/tistory/244CA34E52C6093F31)[![](../images/img_50_02.gif)json-simple-1.1.1.jar](https://t1.daumcdn.net/cfile/tistory/2505AD4E52C609402B)
