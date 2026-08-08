---
title: "[Android] callback button"
date: 2014-01-03 09:06:48 +0900
categories: ["프로그래밍", "Android"]
tags: []
---

> 💡 **TL;DR (핵심 요약)**  
> [Android] callback button에 대한 상세 설명 및 핵심 가이드입니다.

---

## 1. 개요 및 배경

[Android] callback button 가이드 및 실무 적용 설명입니다.

---

## 2. 핵심 설정 및 실행 가이드

```
    
    package kr.priv; 
      
    import android.app.Activity; 
    import android.os.Bundle; 
    import android.widget.TextView; 
      
    public class Test_handler_btnActivity extends Activity { 
        TextView show; 
        @Override
        public void onCreate(Bundle savedInstanceState) { 
            super.onCreate(savedInstanceState); 
            setContentView(R.layout.main); 
              
            MD_test test = new MD_test(); 
            show = (TextView)findViewById(R.id.show); 
              
            MD_test.OnReceiveResult callback = new MD_test.OnReceiveResult() { 
                  
                @Override
                public void onReceiveStream(int timeStamp) { 
                    // TODO Auto-generated method stub 
                    show.setText(">"+timeStamp); 
                      
                } 
            }; 
              
            test.setOnReceiveResult(callback); 
              
              
        } 
    }
    
    ```
    
    
    
    ```
    
    package kr.priv; 
      
    import android.os.Handler; 
    import android.os.Message; 
      
    public class MD_test { 
          
        interface OnReceiveResult { 
            void onReceiveStream(int timeStamp); 
        } 
      
        private OnReceiveResult mCallback; 
      
        public void setOnReceiveResult(OnReceiveResult callback) { 
            mCallback = callback; 
            ServerModeThread tread = new ServerModeThread(); 
            tread.start(); 
        } 
      
        int cnt = 0; 
        private class ServerModeThread extends Thread { 
            public void run(){ 
                  
                while (true) { 
                    try { 
                          
                        handler.sendEmptyMessage(0); 
                        Thread.sleep(1000); 
                    } catch (InterruptedException e) { 
                        // TODO Auto-generated catch block 
                        e.printStackTrace(); 
                    } 
                } 
                  
            } 
        } 
          
        Handler handler = new Handler() { 
            public void handleMessage(Message msg) { 
                if (msg.what == 0) { 
      
                    cnt++; 
                    mCallback.onReceiveStream(cnt); 
      
                } 
            } 
        }; 
    }
    
    ```

---

## 3. 요약 및 참고사항

- 본 포스트는 실무 개발 및 인프라 운용 중 검증된 노하우를 바탕으로 정리되었습니다.
- 추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요.
